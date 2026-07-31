#!/usr/bin/env python3
"""
Stitch chunk images (created by split_map.py) back into one large image.

Writes `static/map_stitched.png` using `static/chunks/manifest.json`.
"""
import json
from pathlib import Path
from PIL import Image


def stitch(manifest_path: Path, out_path: Path):
    with manifest_path.open('r', encoding='utf-8') as f:
        manifest = json.load(f)

    cols = manifest['cols']
    rows = manifest['rows']
    chunks = manifest['chunks']

    if not chunks:
        raise SystemExit('No chunks in manifest')

    # Determine tile size from first chunk bbox
    first = chunks[0]
    left, top, right, bottom = first['bbox']
    tile_w = right - left
    tile_h = bottom - top

    total_w = tile_w * cols
    total_h = tile_h * rows

    out = Image.new('RGBA', (total_w, total_h))

    for entry in chunks:
        r = entry['row']
        c = entry['col']
        file_rel = entry['file'].replace('\\', '/')
        chunk_path = manifest_path.parent / Path(file_rel).name
        if not chunk_path.exists():
            print('Missing chunk:', chunk_path)
            continue
        img = Image.open(chunk_path).convert('RGBA')
        x = c * tile_w
        y = r * tile_h
        out.paste(img, (x, y))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.save(out_path)
    print('Wrote stitched image:', out_path)


def main():
    base = Path('static/chunks')
    manifest = base / 'manifest.json'
    out = Path('static') / 'map_stitched.png'
    if not manifest.exists():
        print('Manifest not found at', manifest)
        return
    stitch(manifest, out)


if __name__ == '__main__':
    main()
