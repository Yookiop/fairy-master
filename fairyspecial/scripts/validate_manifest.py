#!/usr/bin/env python3
"""Validate the `static/chunks/manifest.json` structure and the stitched image dimensions.

Prints any mismatches and suggestions.
"""
import json
from pathlib import Path
from PIL import Image


def main():
    manifest_path = Path('static/chunks/manifest.json')
    if not manifest_path.exists():
        print('Manifest not found at', manifest_path)
        return

    with manifest_path.open('r', encoding='utf-8') as f:
        manifest = json.load(f)

    chunks = manifest.get('chunks', [])
    if not chunks:
        print('No chunks found in manifest')
        return

    first = chunks[0]
    w = first['bbox'][2] - first['bbox'][0]
    h = first['bbox'][3] - first['bbox'][1]

    print('Chunks in manifest:', len(chunks))
    print('Expected cols x rows:', manifest.get('cols'), 'x', manifest.get('rows'))
    print('First chunk bbox size (w x h):', w, 'x', h)

    all_square = True
    for e in chunks:
        left, top, right, bottom = e['bbox']
        cw = right - left
        ch = bottom - top
        if cw != ch:
            all_square = False
            print(f"Chunk {e['row']},{e['col']} not square: {cw}x{ch}")

    if all_square:
        print('All chunks are square')
    else:
        print('At least one chunk is not square - consider re-running split_map.py with --tile-px or --pad')

    # check stitched image
    stitched = Path('static/map_stitched.png')
    if stitched.exists():
        im = Image.open(stitched)
        iw, ih = im.size
        cols = manifest.get('cols')
        rows = manifest.get('rows')
        if cols and rows:
            expected_w = w * cols
            expected_h = h * rows
            if iw != expected_w or ih != expected_h:
                print('Stitched image size mismatch: expected', expected_w, 'x', expected_h, 'but got', iw, 'x', ih)
            else:
                print('Stitched image dimensions OK')
            # additionally, if the stitch suggests a different row count based on tile h, compute it
            if h > 0:
                derived_rows = ih // h
                if derived_rows != rows:
                    print(f"Derived rows from stitched image != manifest rows ({derived_rows} != {rows}) - consider re-run split_map.py with --rows {derived_rows}")
    else:
        print('Stitched image not found at static/map_stitched.png')


if __name__ == '__main__':
    main()
