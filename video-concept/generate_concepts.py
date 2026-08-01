# Generates 1920x1080 video concept images for FairyMaster ("locked to the fairy ring chunks")
# Built from the REAL map tiles in fairyspecial/static/chunks.
import json, os, math, re
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

BASE = r'c:\administratie\git\FairyMaster\fairyspecial\static\chunks'
OUT = r'c:\administratie\git\FairyMaster\video-concept'
os.makedirs(OUT, exist_ok=True)

manifest = json.load(open(os.path.join(BASE, 'manifest.json')))
COLS, ROWS = manifest['cols'], manifest['rows']

# Fairy ring chunks (same set as FAIRY_CHUNKS in index.html)
FAIRY = {
    '4,9', '4,23', '6,4', '6,26', '7,6', '8,20', '8,23', '8,27', '9,12', '9,26',
    '10,4', '10,25', '10,32', '10,37', '10,40', '11,38', '12,26', '13,6', '13,25', '13,37',
    '14,25', '14,26', '14,32', '15,32', '16,18', '16,23', '16,25', '16,29', '16,30', '16,34',
    '17,9', '17,17', '17,21', '17,37', '18,19', '18,24', '18,27', '19,5', '22,26', '22,35', '26,33'
}
CHUNK_PX = 256  # each chunk is 256x256 px

# Ring game coords -> calibrated stitched-map position, SAME as the app:
# colWidths 256px, rows scaled to 97% = 248px (DEFAULT_ROW_SCALE_PERCENT=97).
# Verified against the app's DOM marker positions (CIS=(2424,1128), CLP y=3689, ...).
INDEX_JS = r'c:\administratie\git\FairyMaster\fairyspecial\static\index.js'
TILE, MIN_X, MAX_Y, XC = 64, 1024, 4160, -6
ROW_H = 248  # 256 * 0.97 rounded

def load_rings():
    js = open(INDEX_JS, encoding='utf-8').read()
    block = re.search(r"const FAIRY_RING_LOCATIONS = Object\.freeze\(\{(.*?)\}\);", js, re.S).group(1)
    rings = []
    for m in re.finditer(r"'(\w+)':\s*\{ chunkId: 'chunk_(\d+)_(\d+)', dest: (?:'[^']*'|\"[^\"]*\"), x: (\d+), y: (\d+) \}", block):
        code, r, c, x, y = m.groups()
        r, c, x, y = int(r), int(c), int(x), int(y)
        if f'{r},{c}' not in FAIRY:
            continue
        fx = (x + XC - (MIN_X + c * TILE)) / TILE
        fy = ((MAX_Y - r * TILE) - y) / TILE
        rings.append((c * CHUNK_PX + fx * CHUNK_PX, r * ROW_H + fy * ROW_H))
    return rings

def build_overview(scale):
    """Compose the full map (46x31 grid) at the given scale (chunk size = 256/scale)."""
    cs = CHUNK_PX // scale
    img = Image.new('RGB', (COLS * cs, ROWS * cs))
    for ch in manifest['chunks']:
        r, c = ch['row'], ch['col']
        im = Image.open(os.path.join(BASE, os.path.basename(ch['file'])))
        if im.size != (CHUNK_PX, CHUNK_PX):
            im = im.resize((CHUNK_PX, CHUNK_PX), Image.LANCZOS)
        img.paste(im.resize((cs, cs), Image.LANCZOS), (c * cs, r * cs))
    return img

def build_region(r0, r1, c0, c1):
    """Compose a high-res region (full 256px chunks) for rows r0..r1, cols c0..c1."""
    w = (c1 - c0 + 1) * CHUNK_PX
    h = (r1 - r0 + 1) * CHUNK_PX
    img = Image.new('RGB', (w, h))
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            fn = os.path.join(BASE, f'chunk_{r}_{c}.png')
            if os.path.exists(fn):
                img.paste(Image.open(fn).resize((CHUNK_PX, CHUNK_PX), Image.LANCZOS), ((c - c0) * CHUNK_PX, (r - r0) * CHUNK_PX))
    return img

def font(size, bold=True):
    names = ([r'C:\Windows\Fonts\arialbd.ttf'] if bold else []) + [
        r'C:\Windows\Fonts\arial.ttf', r'C:\Windows\Fonts\segoeui.ttf']
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            continue
    return ImageFont.load_default()

def cover(bg, img):
    """Scale img to cover bg and center."""
    bg_w, bg_h = bg.size
    scale = max(bg_w / img.width, bg_h / img.height)
    nw, nh = int(img.width * scale), int(img.height * scale)
    img = img.resize((nw, nh), Image.LANCZOS)
    x = (bg_w - nw) // 2
    y = (bg_h - nh) // 2
    bg.paste(img, (x, y))

def darken(img, factor):
    return ImageEnhance.Brightness(img).enhance(factor)

def draw_outline_text(d, xy, text, fnt, fill, outline):
    x, y = xy
    for dx in (-3, 0, 3):
        for dy in (-3, 0, 3):
            d.text((x + dx, y + dy), text, font=fnt, fill=outline, anchor='ma')
    d.text((x, y), text, font=fnt, fill=fill, anchor='ma')

def rounded_rect(d, box, radius, fill=None, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def draw_padlock(d, cx, cy, size, color):
    """Draw a padlock centered at (cx, cy)."""
    body_w = size
    body_h = int(size * 0.72)
    bx0, by0 = cx - body_w // 2, cy - body_h // 2 + int(size * 0.06)
    d.rounded_rectangle([bx0, by0, bx0 + body_w, by0 + body_h], radius=int(body_w * 0.14), fill=color)
    # keyhole
    kh = int(body_h * 0.4)
    d.ellipse([cx - kh // 2, by0 + int(body_h * 0.25), cx + kh // 2, by0 + int(body_h * 0.25) + kh], fill=(10, 12, 20))
    d.rectangle([cx - kh // 6, by0 + int(body_h * 0.45), cx + kh // 6, by0 + int(body_h * 0.85)], fill=(10, 12, 20))
    # shackle
    sw = int(body_w * 0.42)
    sh = int(size * 0.42)
    d.arc([cx - sw // 2, cy - int(size * 0.42) - sh // 2, cx + sw // 2, cy - int(size * 0.42) + sh // 2],
          start=180, end=360, fill=color, width=max(6, int(body_w * 0.13)))

def load_ring_icon():
    p = r'c:\administratie\git\FairyMaster\fairyspecial\static\boss_images\fairy_ring_travel.png'
    if os.path.exists(p):
        return Image.open(p).convert('RGBA')
    return None

# ---------------------------------------------------------------------------
print('Building overview (1/8)...')
overview_small = build_overview(8)   # 1472 x 992
overview_small.save(os.path.join(OUT, '_overview_full.png'))

print('Building high-res region (rows 13-17, cols 27-36)...')
region = build_region(13, 17, 27, 36)  # 10 cols x 5 rows -> 2560 x 1280
region.save(os.path.join(OUT, '_region_hr.png'))

W, H = 1920, 1080
CYAN = (0, 229, 255)
GREEN = (46, 204, 113)
WHITE = (240, 244, 248)

# ===========================================================================
# IMAGE 1 - Title / thumbnail card
# ===========================================================================
print('Image 1: title card...')
img = Image.new('RGB', (W, H), (10, 12, 18))
cover(img, region)
img = darken(img, 0.42)
# dim outside a center focal area a bit more for text contrast
d = ImageDraw.Draw(img, 'RGBA')
d.rectangle([0, 0, W, H], fill=(0, 0, 0, 120))
# green borders on fairy chunks visible in region (chunk coords -> region pixels, then scaled)
region_c0, region_r0 = 27, 13
cs_full = 256
def chunk_px_in_region(r, c):
    # position inside the region image (full res)
    return ((c - region_c0) * cs_full, (r - region_r0) * cs_full)
# scale region->canvas
scale_canvas = max(W / region.width, H / region.height)
offx = (W - region.width * scale_canvas) // 2
offy = (H - region.height * scale_canvas) // 2
for r in range(13, 18):
    for c in range(27, 37):
        if f'{r},{c}' in FAIRY:
            px, py = chunk_px_in_region(r, c)
            x0 = offx + px * scale_canvas
            y0 = offy + py * scale_canvas
            d.rectangle([x0, y0, x0 + 256 * scale_canvas, y0 + 256 * scale_canvas],
                        outline=GREEN, width=max(2, int(4.95 * scale_canvas)))
# title
f_title = font(170)
f_sub = font(52)
f_tag = font(30, bold=False)
f_ring = font(34)
draw_outline_text(d, (W // 2, 300), 'FAIRYMASTER', f_title, CYAN, (0, 0, 0))
draw_outline_text(d, (W // 2, 520), 'LOCKED TO THE FAIRY RING CHUNKS', f_sub, WHITE, (0, 0, 0))
# ring icon next to a small line
icon = load_ring_icon()
if icon:
    icon = icon.resize((90, 90), Image.LANCZOS)
    d.ellipse([W // 2 - 200, 640, W // 2 - 110, 730], fill=(0, 0, 0, 140))
    img.paste(icon, (W // 2 - 195, 645), icon)
d.text((W // 2 - 30, 688), 'fairy-ring travel', font=f_tag, fill=(180, 200, 210), anchor='lm')
d.text((W // 2, 900), 'AN OSRS WORLD-MAP TOOL', font=f_ring, fill=(120, 140, 150), anchor='mm')
img.save(os.path.join(OUT, '01-title-card.png'))
print('  saved 01-title-card.png')

# ===========================================================================
# IMAGE 2 - "Locked to the fairy ring chunks" concept
# ===========================================================================
print('Image 2: locked concept...')
img = Image.new('RGB', (W, H), (8, 10, 16))
cover(img, overview_small)
# dim non-fairy chunks, keep fairy chunks bright
cs_small = CHUNK_PX // 8
ov_scale = max(W / overview_small.width, H / overview_small.height)
ox = (W - overview_small.width * ov_scale) // 2
oy = (H - overview_small.height * ov_scale) // 2
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov, 'RGBA')
for r in range(ROWS):
    for c in range(COLS):
        x0 = ox + c * cs_small * ov_scale
        y0 = oy + r * cs_small * ov_scale
        if f'{r},{c}' in FAIRY:
            d.rectangle([x0, y0, x0 + cs_small * ov_scale, y0 + cs_small * ov_scale],
                        fill=(46, 204, 113, 46), outline=GREEN, width=2)
        else:
            d.rectangle([x0, y0, x0 + cs_small * ov_scale, y0 + cs_small * ov_scale], fill=(0, 0, 0, 175))
img.paste(ov, (0, 0), ov)
# padlock + caption
d = ImageDraw.Draw(img, 'RGBA')
draw_padlock(d, W // 2, 430, 190, (0, 229, 255))
f_h1 = font(84)
f_h2 = font(44)
f_body = font(34, bold=False)
draw_outline_text(d, (W // 2, 610), 'THE WORLD IS LOCKED', f_h1, CYAN, (0, 0, 0))
draw_outline_text(d, (W // 2, 715), 'to the 41 fairy ring chunks', f_h2, WHITE, (0, 0, 0))
# legend
lg_y = 850
d.rectangle([W // 2 - 470, lg_y - 24, W // 2 - 400, lg_y + 46], fill=(46, 204, 113, 80), outline=GREEN, width=3)
d.text((W // 2 - 380, lg_y + 10), '41 active fairy ring chunks', font=f_body, fill=WHITE, anchor='lm')
d.rectangle([W // 2 + 40, lg_y - 24, W // 2 + 110, lg_y + 46], fill=(0, 0, 0, 200), outline=(70, 80, 95), width=3)
d.text((W // 2 + 130, lg_y + 10), 'dormant terrain', font=f_body, fill=(160, 170, 180), anchor='lm')
img.save(os.path.join(OUT, '02-locked-to-fairy-rings.png'))
print('  saved 02-locked-to-fairy-rings.png')

# ===========================================================================
# IMAGE 3 - Fairy ring travel network
# ===========================================================================
print('Image 3: travel network...')
img = Image.new('RGB', (W, H), (8, 10, 16))
cover(img, overview_small)
img = darken(img, 0.6)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov, 'RGBA')
# node centers (canvas coords)
nodes = []
for (sx, sy) in load_rings():
    cx = ox + (sx / 8) * ov_scale
    cy = oy + (sy / 8) * ov_scale
    nodes.append((cx, cy))
# Clean network via a Minimum Spanning Tree: connects all 41 rings with the
# fewest/shortest lines instead of a dense web (especially in the middle).
parent = list(range(len(nodes)))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    parent[ra] = rb
    return True
edges = []
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        dist = math.hypot(nodes[j][0] - nodes[i][0], nodes[j][1] - nodes[i][1])
        edges.append((dist, i, j))
edges.sort()
for dist, i, j in edges:
    if union(i, j):
        x1, y1 = nodes[i]
        x2, y2 = nodes[j]
        d.line([x1, y1, x2, y2], fill=(0, 229, 255, 170), width=4)
img.paste(ov, (0, 0), ov)
# fairy ring icon at every node (bigger, no text, no green squares)
ring_icon = load_ring_icon()
if ring_icon:
    isz = max(18, int(cs_small * ov_scale * 0.85))
    ring_icon = ring_icon.resize((isz, isz), Image.LANCZOS)
    for (cx, cy) in nodes:
        img.paste(ring_icon, (int(cx - isz / 2), int(cy - isz / 2)), ring_icon)
img.save(os.path.join(OUT, '03-fairy-ring-network.png'))
print('  saved 03-fairy-ring-network.png')

# ===========================================================================
# IMAGE 4 - Close-up "chunk lock" example (in-app look)
# ===========================================================================
print('Image 4: close-up chunk example...')
# use high-res region, crop to a nice 16:9 area around rows 14-16 cols 29-35
sub = region.crop(((29 - 27) * 256, (14 - 13) * 256, (36 - 27) * 256, (17 - 13) * 256))  # cols29-36, rows14-17
img = Image.new('RGB', (W, H), (8, 10, 16))
cover(img, sub)
img = darken(img, 0.75)
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov, 'RGBA')
sc = max(W / sub.width, H / sub.height)
sx = (W - sub.width * sc) // 2
sy = (H - sub.height * sc) // 2
# green borders + labels for the fairy chunks in view
codes = {
    '14,29': 'DKR', '14,32': 'CLP', '15,32': 'DIS', '16,29': 'DKP',
    '16,30': 'AIQ', '16,34': 'BIQ', '16,25': 'CLS', '14,25': 'DJP',
}
f_label = font(46)
for r in range(14, 17):
    for c in range(29, 36):
        key = f'{r},{c}'
        if key in FAIRY:
            x0 = sx + (c - 29) * 256 * sc
            y0 = sy + (r - 14) * 256 * sc
            d.rectangle([x0, y0, x0 + 256 * sc, y0 + 256 * sc], fill=(46, 204, 113, 40), outline=GREEN, width=max(2, int(5 * sc)))
            code = codes.get(key, '???')
            # black label box + cyan text
            lw = 3.2 * 256 * sc * 0.16
            lh = 256 * sc * 0.16 * 1.5
            lx = x0 + 256 * sc - lw - 10
            ly = y0 + (256 * sc - lh) / 2
            d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=8, fill=(0, 0, 0, 190))
            d.text((lx + lw / 2, ly + lh / 2), code, font=font(int(256 * sc * 0.11)), fill=CYAN, anchor='mm')
# lock chip top-right
draw_padlock(d, W - 170, 130, 110, (0, 229, 255))
d.rounded_rectangle([W - 320, 205, W - 20, 265], radius=14, fill=(0, 0, 0, 170), outline=(46, 204, 113), width=3)
d.text((W - 170, 235), 'locked to the chunk', font=font(34), fill=WHITE, anchor='mm')
img.paste(ov, (0, 0), ov)
d = ImageDraw.Draw(img, 'RGBA')
f_t2 = font(64)
draw_outline_text(d, (W // 2, 70), 'EVERY FAIRY RING = ONE LOCKED CHUNK', f_t2, CYAN, (0, 0, 0))
img.save(os.path.join(OUT, '04-chunk-lock-example.png'))
print('  saved 04-chunk-lock-example.png')

print('Done! Images written to', OUT)
