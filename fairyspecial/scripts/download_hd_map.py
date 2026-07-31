#!/usr/bin/env python3
"""Download the full-resolution OSRS world map from the Wiki."""
import urllib.request
import sys
from pathlib import Path

URL = "https://oldschool.runescape.wiki/images/Old_School_RuneScape_world_map.png?b3666"
OUT = Path(__file__).parent.parent / "Old_School_RuneScape_world_map_hd.png"

def main():
    # First check headers
    req = urllib.request.Request(URL, method='HEAD')
    req.add_header('User-Agent', 'BossChunkNew/1.0 (OSRS map tool)')
    try:
        resp = urllib.request.urlopen(req)
        cl = resp.headers.get('Content-Length', '0')
        print(f"Status: {resp.status}")
        print(f"Content-Length: {int(cl):,} bytes ({int(cl)/1024/1024:.1f} MB)")
        print(f"Content-Type: {resp.headers.get('Content-Type')}")
    except Exception as e:
        print(f"HEAD request failed: {e}")
        return

    # Check if we already have this file with correct size
    if OUT.exists():
        expected_size = int(cl)
        actual_size = OUT.stat().st_size
        if actual_size == expected_size:
            print(f"\nFile already exists with correct size: {OUT}")
            print(f"Size: {actual_size:,} bytes")
            from PIL import Image
            img = Image.open(OUT)
            print(f"Resolution: {img.size[0]}x{img.size[1]}")
            return
        else:
            print(f"\nExisting file has wrong size ({actual_size:,} vs expected {expected_size:,}), re-downloading...")

    # Download with proper headers
    print(f"\nDownloading to: {OUT}")
    try:
        req = urllib.request.Request(URL)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) BossChunkNew/1.0')
        req.add_header('Referer', 'https://oldschool.runescape.wiki/')
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            OUT.write_bytes(data)
        print(f"Downloaded: {OUT.stat().st_size:,} bytes")
        # Verify
        from PIL import Image
        img = Image.open(OUT)
        print(f"Resolution: {img.size[0]}x{img.size[1]}")
    except Exception as e:
        print(f"Download failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
