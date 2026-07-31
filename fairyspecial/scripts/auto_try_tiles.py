#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import sys

ROOT = Path(__file__).resolve().parents[1]
# helper to load module from path
def load_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

split_mod = load_module_from_path('split_map', ROOT / 'scripts' / 'split_map.py')
stitch_mod = load_module_from_path('stitch_map', ROOT / 'scripts' / 'stitch_map.py')

src = ROOT / 'Old_School_RuneScape_world_map.png'
if not src.exists():
    # try to find any large png in repo root
    candidates = list(ROOT.glob('*.png'))
    if candidates:
        src = candidates[0]
        print('Using source image:', src)
    else:
        print('Source map image not found in repo root. Place the original map next to scripts or pass it manually.'); sys.exit(1)

out_dir_base = ROOT / 'static'

for tile_px in (4,8):
    print('\n=== Trying tile_px=', tile_px, '===')
    out_chunks = ROOT / 'static' / f'chunks_tmp_px{tile_px}'
    if out_chunks.exists():
        # clear
        for p in out_chunks.glob('*'):
            try: p.unlink()
            except Exception: pass
    try:
        split_mod.split_image(src, out_chunks, cols=46, rows=31, prefix='chunk_', tile_px=tile_px, pad=True)
    except Exception as e:
        print('split_image failed for', tile_px, e)
        continue
    manifest = out_chunks / 'manifest.json'
    out_stitched = out_dir_base / f'map_stitched_px{tile_px}.png'
    try:
        stitch_mod.stitch(manifest, out_stitched)
    except Exception as e:
        print('stitch failed for', tile_px, e)
        continue
    print('Wrote stitched for tile_px', tile_px, '->', out_stitched)

print('\nDone. Check static/map_stitched_px4.png and static/map_stitched_px8.png')
