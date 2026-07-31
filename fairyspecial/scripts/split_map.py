#!/usr/bin/env python3
"""
Split a world map image into a grid of chunks.

Defaults split into 46 columns × 31 rows and writes PNG chunks to `static/chunks/`.
Also writes `static/chunks/manifest.json` containing rows/cols and filenames.
"""
import argparse
import json
import math
from pathlib import Path
from PIL import Image


def split_image(src_path: Path, out_dir: Path, cols: int, rows: int, prefix: str = "chunk_", tile_px: int = None, pad: bool = False):
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = {"cols": cols, "rows": rows, "chunks": []}

    # Determine the target chunk pixel size so each chunk is square and corresponds to 64x64 tiles
    # tile_px: pixels per in-game tile (optional). If unspecified, infer tile_px so chunk_px >= original chunk width/height (avoids cropping)
    orig_w, orig_h = img.size
    chunk_w = orig_w / cols
    chunk_h = orig_h / rows
    if tile_px is None:
        # choose a tile_px such that chunk_px >= original chunk width and height to avoid cropping
        inferred_tile_px = int(math.ceil(max(chunk_w, chunk_h) / 64))
        if inferred_tile_px < 1:
            raise ValueError(f"Computed tile_px < 1 - image too small or too many cols/rows: chunk_w={chunk_w}, chunk_h={chunk_h}")
        tile_px = inferred_tile_px

    chunk_px = tile_px * 64
    print(f"Using tile_px={tile_px} -> chunk_px={chunk_px} (pixels per chunk)")
    target_w = int(cols * chunk_px)
    target_h = int(rows * chunk_px)
    if (target_w, target_h) != (orig_w, orig_h):
        if pad:
            print(f"Padding source image from {orig_w}x{orig_h} -> {target_w}x{target_h} to ensure square chunk_px={chunk_px}")
            new_img = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
            # paste original at top-left so coordinates remain consistent
            new_img.paste(img, (0, 0))
            img = new_img
        else:
            print(f"Resizing source image from {orig_w}x{orig_h} -> {target_w}x{target_h} to ensure square chunk_px={chunk_px}")
            img = img.resize((target_w, target_h), Image.LANCZOS)

    for r in range(rows):
        for c in range(cols):
            # now we can compute strictly square chunk pixel bounds as multiples of chunk_px
            left = int(c * chunk_px)
            right = int((c + 1) * chunk_px)
            top = int(r * chunk_px)
            bottom = int((r + 1) * chunk_px)

            crop = img.crop((left, top, right, bottom))
            filename = f"{prefix}{r}_{c}.png"
            out_path = out_dir / filename
            crop.save(out_path, format="PNG")

            manifest["chunks"].append({
                "row": r,
                "col": c,
                "file": str(Path(out_dir.name) / filename),
                "bbox": [left, top, right, bottom],
            })

    manifest_path = out_dir / "manifest.json"
    with manifest_path.open("w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Wrote {len(manifest['chunks'])} chunks to: {out_dir}")
    print(f"Manifest: {manifest_path}")


def main():
    p = argparse.ArgumentParser(description="Split a world map image into a grid of chunks")
    p.add_argument("src", nargs="?", default="Old_School_RuneScape_world_map.png",
                   help="Source world map image (default: Old_School_RuneScape_world_map.png)")
    p.add_argument("--out", default="static/chunks", help="Output directory for chunk images")
    p.add_argument("--cols", type=int, default=46, help="Number of columns (default 46)")
    p.add_argument("--rows", type=int, default=31, help="Number of rows (default 31)")
    p.add_argument("--prefix", default="chunk_", help="Filename prefix for chunk images")
    p.add_argument("--tile-px", type=int, default=None, help="(optional) pixels per in-game tile; if omitted script will infer tile_px to preserve square chunks (64 tiles/chunk)")
    p.add_argument("--pad", action='store_true', help="Pad the source image to the required dimensions instead of resizing. Padding preserves original pixels (transparent background used).")
    args = p.parse_args()

    src_path = Path(args.src)
    if not src_path.exists():
        print(f"Source image not found: {src_path}")
        return

    out_dir = Path(args.out)
    split_image(src_path, out_dir, args.cols, args.rows, args.prefix, args.tile_px, args.pad)


if __name__ == "__main__":
    main()
