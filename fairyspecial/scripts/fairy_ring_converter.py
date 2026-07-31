#!/usr/bin/env python3
"""
Convert RuneLite FairyRingLocation WorldPoint coordinates to BossChunkNew chunk IDs.
World map bounds: X=1024..3968, Y=2048..4032
Chunk grid: 46 cols × 31 rows, each chunk = 64×64 tiles
col = floor((x - 1024) / 64), row = floor((4032 - y) / 64)
"""
import json

# Fairy ring data from RuneLite FairyRingLocation.java
fairy_rings = {
    "AIQ": {"x": 2995, "y": 3112, "dest": "Mudskipper Point"},
    "AIR": {"x": 2699, "y": 3249, "dest": "Island SE of Ardougne"},
    "AIS": {"x": 1430, "y": 3323, "dest": "Auburn Valley"},
    "AJP": {"x": 1648, "y": 3011, "dest": "Avium Savannah"},
    "AJR": {"x": 2779, "y": 3615, "dest": "Slayer cave"},
    "AJS": {"x": 2499, "y": 3898, "dest": "Penguins near Miscellania"},
    "AKP": {"x": 3283, "y": 2704, "dest": "Necropolis"},
    "AKQ": {"x": 2318, "y": 3617, "dest": "Piscatoris Hunter area"},
    "AKR": {"x": 1823, "y": 3539, "dest": "Hosidius Vinery"},
    "AKS": {"x": 2570, "y": 2958, "dest": "Feldip Hunter area"},
    "ALP": {"x": 2502, "y": 3638, "dest": "Lighthouse island"},
    "ALQ": {"x": 3598, "y": 3496, "dest": "Haunted Woods E of Canifis"},
    "ALR": {"x": 3059, "y": 4877, "dest": "Abyssal Area"},
    "ALS": {"x": 2643, "y": 3497, "dest": "McGrubor's Wood"},
    "BIP": {"x": 3409, "y": 3326, "dest": "Island SW of Mort Myre"},
    "BIQ": {"x": 3248, "y": 3095, "dest": "Kalphite Hive"},
    "BIS": {"x": 2635, "y": 3268, "dest": "Ardougne Zoo - Unicorns"},
    "BJP": {"x": 2264, "y": 2976, "dest": "Isle of Souls"},
    "BJS": {"x": 2147, "y": 3069, "dest": "Near Zul-Andra"},
    "BKP": {"x": 2384, "y": 3037, "dest": "South of Castle Wars"},
    "BKR": {"x": 3468, "y": 3433, "dest": "Mort Myre Swamp S of Canifis"},
    "BKS": {"x": 2411, "y": 4436, "dest": "Zanaris"},
    "BLP": {"x": 2432, "y": 5127, "dest": "TzHaar area"},
    "BLR": {"x": 2739, "y": 3353, "dest": "Legends' Guild"},
    "BLS": {"x": 1293, "y": 3495, "dest": "S of Mount Quidamortem"},
    "CIP": {"x": 2512, "y": 3886, "dest": "Miscellania island"},
    "CIQ": {"x": 2527, "y": 3129, "dest": "NW of Yanille"},
    "CIR": {"x": 1303, "y": 3762, "dest": "NE of Farming Guild"},
    "CIS": {"x": 1636, "y": 3869, "dest": "N of Arceuus Library"},
    "CJQ": {"x": 3178, "y": 2445, "dest": "The Great Conch"},
    "CJR": {"x": 2704, "y": 3578, "dest": "Sinclair Mansion"},
    "CKQ": {"x": 1358, "y": 2943, "dest": "Aldarin"},
    "CKR": {"x": 2800, "y": 3005, "dest": "S of Tai Bwo Wannai"},
    "CKS": {"x": 3446, "y": 3472, "dest": "Canifis"},
    "CLP": {"x": 3081, "y": 3208, "dest": "Island S of Draynor Village"},
    "CLR": {"x": 2737, "y": 2739, "dest": "Ape Atoll island"},
    "CLS": {"x": 2681, "y": 3083, "dest": "Hazelmere's home island"},
    "DIP": {"x": 3036, "y": 4761, "dest": "Abyssal Nexus (Sire)"},
    "DIS": {"x": 3109, "y": 3149, "dest": "Wizards' Tower"},
    "DJP": {"x": 2657, "y": 3232, "dest": "Tower of Life"},
    "DJR": {"x": 1452, "y": 3659, "dest": "Chasm of Fire"},
    "DKP": {"x": 2899, "y": 3113, "dest": "S of Musa Point"},
    "DKR": {"x": 3126, "y": 3496, "dest": "Edgeville, Grand Exchange"},
    "DKS": {"x": 2743, "y": 3721, "dest": "Polar Hunter area"},
    "DLP": {"x": 2923, "y": 10455, "dest": "Grimstone Dungeon"},
    "DLQ": {"x": 3422, "y": 3018, "dest": "N of Nardah"},
    "DLR": {"x": 2212, "y": 3101, "dest": "Poison Waste S of Isafdar"},
}

MIN_X = 1024
MAX_Y = 4160
TILE_SIZE = 64
MAX_COLS = 46
MAX_ROWS = 31

results = []
out_of_bounds = []

for code, data in fairy_rings.items():
    x, y, dest = data["x"], data["y"], data["dest"]
    col = (x - MIN_X) // TILE_SIZE
    row = (MAX_Y - y) // TILE_SIZE
    
    if 0 <= col < MAX_COLS and 0 <= row < MAX_ROWS:
        chunk_id = f"chunk_{row}_{col}"
        results.append({
            "code": code,
            "chunkId": chunk_id,
            "row": row,
            "col": col,
            "dest": dest,
            "x": x,
            "y": y
        })
    else:
        out_of_bounds.append({
            "code": code,
            "dest": dest,
            "x": x,
            "y": y,
            "wouldBeRow": row,
            "wouldBeCol": col
        })

print("=== IN-BOUNDS FAIRY RINGS ===")
for r in sorted(results, key=lambda r: (r["row"], r["col"])):
    print(f"  {r['code']}: chunk_{r['row']}_{r['col']} ({r['dest']}) [game: {r['x']},{r['y']}]")

print(f"\n=== OUT-OF-BOUNDS (not on surface map) ===")
for r in out_of_bounds:
    print(f"  {r['code']}: would be chunk_{r['wouldBeRow']}_{r['wouldBeCol']} ({r['dest']}) [game: {r['x']},{r['y']}]")

print(f"\nTotal in-bounds: {len(results)}")
print(f"Total out-of-bounds: {len(out_of_bounds)}")

# Generate JS code
print("\n=== JAVASCRIPT DATA ===")
print("const FAIRY_RING_LOCATIONS = {")
for r in sorted(results, key=lambda r: (r["row"], r["col"])):
    print(f"    '{r['code']}': {{ chunkId: '{r['chunkId']}', dest: '{r['dest']}' }},")
print("};")
