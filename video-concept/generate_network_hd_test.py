# HD test version of the fairy-ring travel network image.
# Uses the HD world map directly (resized to the same 46x31 chunk grid) for crisper
# detail than the 1/8-scale chunk overview. Writes to "01-fairy-ring-network copy.png".
import json, os, math, re
from PIL import Image, ImageDraw, ImageEnhance

HD_SRC = r'c:\administratie\git\FairyMaster\fairyspecial\Old_School_RuneScape_world_map_hd.png'
INDEX_JS = r'c:\administratie\git\FairyMaster\fairyspecial\static\index.js'
CHUNKS_DIR = r'c:\administratie\git\FairyMaster\fairyspecial\static\chunks'
OUT = r'c:\administratie\git\FairyMaster\video-concept\01-fairy-ring-network copy.png'

manifest = json.load(open(os.path.join(CHUNKS_DIR, 'manifest.json')))
COLS, ROWS = manifest['cols'], manifest['rows']

FAIRY = {
    '4,9', '4,23', '6,4', '6,26', '7,6', '8,20', '8,23', '8,27', '9,12', '9,26',
    '10,4', '10,25', '10,32', '10,37', '10,40', '11,38', '12,26', '13,6', '13,25', '13,37',
    '14,25', '14,26', '14,32', '15,32', '16,18', '16,23', '16,25', '16,29', '16,30', '16,34',
    '17,9', '17,17', '17,21', '17,37', '18,19', '18,24', '18,27', '19,5', '22,26', '22,35', '26,33'
}

# Build the overview from the HD map directly at half of the stitched size (128px per chunk)
SCALE = 2
OV_W, OV_H = COLS * 256 // SCALE, ROWS * 256 // SCALE
print('Building HD overview', OV_W, 'x', OV_H)
overview = Image.open(HD_SRC).convert('RGB').resize((OV_W, OV_H), Image.LANCZOS)

W, H = 1920, 1080
img = Image.new('RGB', (W, H), (8, 10, 16))
# cover-scale the overview onto the canvas
ov_scale = max(W / OV_W, H / OV_H)
nw, nh = int(OV_W * ov_scale), int(OV_H * ov_scale)
img.paste(overview.resize((nw, nh), Image.LANCZOS), ((W - nw) // 2, (H - nh) // 2))
img = ImageEnhance.Brightness(img).enhance(0.6)

ox = (W - OV_W * ov_scale) / 2
oy = (H - OV_H * ov_scale) / 2

# Ring positions: calibrated exact positions, SAME as the app (colWidths 256px,
# rows scaled 97% = 248px). Verified against the app's DOM marker positions.
TILE, MIN_X, MAX_Y, XC = 64, 1024, 4160, -6
ROW_H = 248  # 256 * 0.97 rounded
# HD-map alignment: affine transform from the standard grid -> HD map, fitted from
# 7 clean sea-mask template matches (west BLS/AIS, north ALP, center CJR, east
# BIP/CKS, south DIS; outliers excluded), residuals <= 1px:
#   x_hd = 0.9584*x + 122.6 ,  y_hd = 0.9419*y + 115.6   (overview px)
HD_SCALE_X = 0.9584
HD_SCALE_Y = 0.9419
HD_OFFSET_X = 122.6
HD_OFFSET_Y = 115.6

def load_rings():
    js = open(INDEX_JS, encoding='utf-8').read()
    block = re.search(r"const FAIRY_RING_LOCATIONS = Object\.freeze\(\{(.*?)\};", js, re.S).group(1)
    rings = []
    for m in re.finditer(r"'(\w+)':\s*\{ chunkId: 'chunk_(\d+)_(\d+)', dest: (?:'[^']*'|\"[^\"]*\"), x: (\d+), y: (\d+) \}", block):
        code, r, c, x, y = m.groups()
        r, c, x, y = int(r), int(c), int(x), int(y)
        if f'{r},{c}' not in FAIRY:
            continue
        fx = (x + XC - (MIN_X + c * TILE)) / TILE
        fy = ((MAX_Y - r * TILE) - y) / TILE
        rings.append((c * 256 + fx * 256, r * ROW_H + fy * ROW_H))
    return rings

nodes = []
for (sx, sy) in load_rings():
    ov_x = (sx / SCALE) * HD_SCALE_X + HD_OFFSET_X
    ov_y = (sy / SCALE) * HD_SCALE_Y + HD_OFFSET_Y
    cx = ox + ov_x * ov_scale
    cy = oy + ov_y * ov_scale
    nodes.append((cx, cy))

# Minimum Spanning Tree (Kruskal) - clean network, 40 edges
parent = list(range(len(nodes)))
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a
edges = []
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        edges.append((math.hypot(nodes[j][0] - nodes[i][0], nodes[j][1] - nodes[i][1]), i, j))
edges.sort()
ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov, 'RGBA')
for dist, i, j in edges:
    ra, rb = find(i), find(j)
    if ra != rb:
        parent[ra] = rb
        d.line([nodes[i][0], nodes[i][1], nodes[j][0], nodes[j][1]], fill=(0, 229, 255, 170), width=4)
img.paste(ov, (0, 0), ov)

# fairy ring icons
icon = Image.open(r'c:\administratie\git\FairyMaster\fairyspecial\static\boss_images\fairy_ring_travel.png').convert('RGBA')
chunk_on_canvas = (256 / SCALE) * ov_scale
isz = max(18, int(chunk_on_canvas * 0.85))
icon = icon.resize((isz, isz), Image.LANCZOS)
for (cx, cy) in nodes:
    img.paste(icon, (int(cx - isz / 2), int(cy - isz / 2)), icon)

img.save(OUT)
print('Saved', OUT, img.size)
