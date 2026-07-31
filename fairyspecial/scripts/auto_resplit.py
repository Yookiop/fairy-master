"""
Automate trying multiple --tile-px values for splitting and stitching.
Usage:
  py scripts\auto_resplit.py path\to\source_image.png

The script will (for each candidate tile_px):
 - backup existing `static/chunks` and `static/map_stitched.png`
 - run `py scripts\split_map.py <src> --cols 46 --rows 31 --tile-px <tile_px> --pad --out static/chunks`
 - run `py scripts\stitch_map.py`
 - move outputs to `static/map_stitched-tile<tile_px>.png` and `static/chunks-tile<tile_px>/`

It will NOT delete backups. Requires `py` on PATH (Windows).
"""
import sys, subprocess, shutil, os, time
from pathlib import Path

CANDIDATES = [4, 8]
ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / 'static'
CHUNKS = STATIC / 'chunks'
MAP = STATIC / 'map_stitched.png'

def backup_path(p: Path):
    ts = time.strftime('%Y%m%d-%H%M%S')
    return p.parent / (p.name + '.bak_' + ts)

def run(cmd):
    print('RUN:', ' '.join(cmd))
    r = subprocess.run(cmd)
    return r.returncode == 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: py scripts\\auto_resplit.py path\\to\\source_image.png')
        sys.exit(1)
    src = Path(sys.argv[1])
    if not src.exists():
        print('Source image not found:', src)
        sys.exit(1)

    print('Candidates:', CANDIDATES)
    confirm = input('This will (re)generate chunks and stitched image for each candidate and may overwrite existing static/chunks and static/map_stitched.png. Proceed? (y/N): ')
    if confirm.strip().lower() != 'y':
        print('Aborted')
        sys.exit(0)

    for t in CANDIDATES:
        print('\n=== Trying tile_px =', t, ' (chunk_px =', t*64, ') ===')
        # backup existing
        if CHUNKS.exists():
            dest = backup_path(CHUNKS)
            print('Backing up', CHUNKS, '->', dest)
            shutil.move(str(CHUNKS), str(dest))
        if MAP.exists():
            dest = backup_path(MAP)
            print('Backing up', MAP, '->', dest)
            shutil.move(str(MAP), str(dest))
        # run split_map.py (out defaults to static/chunks but we pass out explicitly)
        cmd_split = ['py', str(ROOT / 'scripts' / 'split_map.py'), str(src), '--cols', '46', '--rows', '31', '--tile-px', str(t), '--pad', '--out', str(CHUNKS)]
        ok = run(cmd_split)
        if not ok:
            print('split_map.py failed for tile_px', t)
            continue
        # run stitch_map.py
        cmd_stitch = ['py', str(ROOT / 'scripts' / 'stitch_map.py')]
        ok = run(cmd_stitch)
        if not ok:
            print('stitch_map.py failed for tile_px', t)
            continue
        # move outputs to tile-specific locations
        out_map = STATIC / f'map_stitched-tile{t}.png'
        if MAP.exists():
            shutil.move(str(MAP), str(out_map))
            print('Saved', out_map)
        out_chunks = STATIC / f'chunks-tile{t}'
        if CHUNKS.exists():
            shutil.move(str(CHUNKS), str(out_chunks))
            print('Saved chunks to', out_chunks)
        # also move manifest if present
        manifest = out_chunks / 'manifest.json'
        if manifest.exists():
            print('Manifest at', manifest)

    print('\nDone. Generated stitched images:')
    for t in CANDIDATES:
        p = STATIC / f'map_stitched-tile{t}.png'
        print('-', p, '(exists)' if p.exists() else '(missing)')
    print('\nBackups preserved as .bak_* in static/ or previous chunks locations.')
