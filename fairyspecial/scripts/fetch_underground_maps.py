"""Fetch the underground / instance fairy ring location images from the OSRS Wiki.

Reads the "Fairy rings" wiki page, extracts the kartographer map tiles for each
underground / instance fairy ring, downloads them and composes a 200x200 PNG per
ring (matching the wiki's rendering). DIQ (Player-owned house superior garden)
uses an illustration instead of map tiles.

Output: static/underground/{CODE}.png  (+ HIDEOUT.png for the Fairy Hideout)

Requires Pillow. Usage:
    python scripts/fetch_underground_maps.py
"""

import io
import json
import os
import re
import sys
import urllib.error
import urllib.request

from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.normpath(os.path.join(BASE_DIR, '..', 'static', 'underground'))

API_URL = 'https://oldschool.runescape.wiki/api.php?action=parse&page=Fairy_rings&prop=text&format=json'
WIKI_BASE = 'https://oldschool.runescape.wiki'
USER_AGENT = 'FairySpecial-map-tool/1.0 (hobby OSRS project)'

SIZE = 200  # composed tile size in px (matches the wiki 200x200 map thumb)

# All underground / instance rings shown in the popup (13 rings + the hideout sequence)
UNDERGROUND_RINGS = ['ALR', 'BKS', 'BLP', 'DIP', 'DLP', 'AJQ', 'BJR', 'BKQ', 'CKP', 'DIQ', 'DIR', 'DLS', 'BLQ']
HIDEOUT_CODES = ['AIR', 'DLR', 'DJQ', 'AJS']


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def fetch_json(url):
    return json.loads(fetch(url).decode('utf-8'))


def fairycode_pattern(code):
    """Match the wiki's fairycode markup, e.g. <b>A</b><b>L</b><b>R</b>."""
    return '<span class="fairycode"><b>' + '</b><b>'.join(code) + '</b></span>'


def split_rows(html):
    return re.findall(r'<tr[^>]*>.*?</tr>', html, re.DOTALL)


COMBINATION_SECTIONS = ['"A" combinations', '"B" combinations', '"C" combinations', '"D" combinations']


def get_sections(html):
    """Split the page into <h3> sections -> {heading_text: content}."""
    sections = {}
    parts = re.split(r'<h3[^>]*>(.*?)</h3>', html, flags=re.DOTALL)
    for i in range(1, len(parts), 2):
        heading = re.sub(r'<[^>]+>', '', parts[i]).strip()
        content = parts[i + 1] if i + 1 < len(parts) else ''
        sections[heading] = content
    return sections


def find_combo_row(sections, code):
    """Find the Combinations-table row for a code (avoids the 'Using fairy rings' table)."""
    pat = fairycode_pattern(code)
    for sec in COMBINATION_SECTIONS:
        for row in split_rows(sections.get(sec, '')):
            if pat in row:
                return row
    return None


def find_hideout_row(sections):
    for row in split_rows(sections.get('Sequences', '')):
        if 'id="Hideout"' in row:
            return row
    return None


def extract_map_tiles(row_html):
    """Return (tile_urls, positions) from a kartographer map element, or None."""
    el_m = re.search(r'<a class="mw-kartographer-map[^>]*>', row_html)
    if not el_m:
        return None
    el = el_m.group(0)
    style_m = re.search(r'style="([^"]*)"', el)
    if not style_m:
        return None
    style = style_m.group(1)
    urls = re.findall(r'url\((https://maps\.runescape\.wiki[^)]+)\)', style)
    positions = []
    pos_m = re.search(r'background-position:\s*([^;]+)', style)
    if pos_m:
        for pair in pos_m.group(1).strip().split(','):
            parts = pair.strip().split()
            if len(parts) >= 2:
                positions.append((int(parts[0].replace('px', '')), int(parts[1].replace('px', ''))))
    if not urls or len(urls) != len(positions):
        return None
    return urls, positions


def extract_illustration_url(row_html):
    """For DIQ: get the original illustration image URL from a thumb src."""
    img_m = re.search(r'<img[^>]+src="(/images/thumb/[^"]+)"', row_html)
    if not img_m:
        return None
    thumb = img_m.group(1).split('?')[0]  # strip query string
    # thumb = /images/thumb/<inner>/<size>px-<filename> ; original = /images/<inner>
    m = re.match(r'^/images/thumb/(.+)/(\d+)px-[^/]+$', thumb)
    if m:
        return WIKI_BASE + '/images/' + m.group(1)
    return WIKI_BASE + thumb


def paste_clip(dst, src, x, y):
    """Paste src onto dst with top-left at (x, y), clipping to dst bounds."""
    sx, sy = 0, 0
    if x < 0:
        sx = -x
        x = 0
    if y < 0:
        sy = -y
        y = 0
    sw = min(src.width - sx, dst.width - x)
    sh = min(src.height - sy, dst.height - y)
    if sw <= 0 or sh <= 0:
        return
    dst.paste(src.crop((sx, sy, sx + sw, sy + sh)), (x, y))


def compose_map_tiles(tile_urls, positions, out_path):
    canvas = Image.new('RGB', (SIZE, SIZE), (0, 0, 0))
    for url, (px, py) in zip(tile_urls, positions):
        try:
            tile = Image.open(io.BytesIO(fetch(url))).convert('RGB')
        except urllib.error.HTTPError as exc:
            # Some void/empty tiles are not rendered by the wiki -> keep black
            print(f'    (missing tile {exc.code}: {os.path.basename(url)} -> black)')
            continue
        except Exception as exc:  # noqa: BLE001
            print(f'    (tile error {url}: {exc})')
            continue
        paste_clip(canvas, tile, px, py)
    canvas.save(out_path, 'PNG')
    print(f'  -> {os.path.basename(out_path)} ({len(tile_urls)} tiles)')


def compose_cover(src_bytes, out_path):
    """Scale an illustration to fill the square (cover) and center-crop it."""
    img = Image.open(io.BytesIO(src_bytes)).convert('RGB')
    scale = SIZE / min(img.size)
    img = img.resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))), Image.LANCZOS)
    left = (img.width - SIZE) // 2
    top = (img.height - SIZE) // 2
    img = img.crop((left, top, left + SIZE, top + SIZE))
    img.save(out_path, 'PNG')
    print(f'  -> {os.path.basename(out_path)} (illustration)')


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print('Fetching Fairy rings wiki page...')
    html = fetch_json(API_URL)['parse']['text']['*']
    sections = get_sections(html)
    print(f'Found sections: {", ".join(sections.keys())}\n')

    ok, fail = [], []

    # 1. Fairy Hideout (Sequences row)
    hideout_row = find_hideout_row(sections)
    if hideout_row:
        tiles = extract_map_tiles(hideout_row)
        if tiles:
            compose_map_tiles(*tiles, os.path.join(OUT_DIR, 'HIDEOUT.png'))
            ok.append('HIDEOUT')
        else:
            fail.append('HIDEOUT (no map tiles)')
    else:
        fail.append('HIDEOUT (row not found)')

    # 2. All other underground rings
    for code in UNDERGROUND_RINGS:
        row = find_combo_row(sections, code)
        if row is None:
            fail.append(f'{code} (row not found)')
            continue
        tiles = extract_map_tiles(row)
        if tiles:
            compose_map_tiles(*tiles, os.path.join(OUT_DIR, f'{code}.png'))
            ok.append(code)
            continue
        # DIQ uses an illustration
        illus = extract_illustration_url(row)
        if illus:
            try:
                compose_cover(fetch(illus), os.path.join(OUT_DIR, f'{code}.png'))
                ok.append(code)
            except Exception as exc:  # noqa: BLE001
                fail.append(f'{code} (illustration failed: {exc})')
        else:
            fail.append(f'{code} (no map or illustration)')

    print(f'\nDone: {len(ok)} OK, {len(fail)} failed.')
    if fail:
        print('Failed:')
        for f in fail:
            print('  -', f)
        sys.exit(1)


if __name__ == '__main__':
    main()
