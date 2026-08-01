from PIL import Image
import os

p = r'c:\administratie\git\FairyMaster\video-concept\01-fairy-ring-network copy.png'
im = Image.open(p).convert('RGB')
W, H = im.size
print('size:', W, 'x', H, 'KB:', os.path.getsize(p) // 1024)

def ring_canvas(r, c, x, y):
    SCALE = 2
    OV_W, OV_H = 5888, 3968
    ov_scale = max(W / OV_W, H / OV_H)
    ox = (W - OV_W * ov_scale) / 2
    oy = (H - OV_H * ov_scale) / 2
    TILE = 64; MIN_X = 1024; MAX_Y = 4160; XC = -6
    fx = (x + XC - (MIN_X + c * TILE)) / TILE
    fy = ((MAX_Y - r * TILE) - y) / TILE
    stx = c * 256 + fx * 256
    sty = r * 256 + fy * 256
    return int(ox + (stx / SCALE + 128 / SCALE) * ov_scale), int(oy + (sty / SCALE + 128 / SCALE) * ov_scale)

tests = [('CLP', 14, 32, 3081, 3208), ('DIS', 15, 32, 3109, 3149), ('BIQ', 16, 34, 3248, 3095),
         ('CIS', 4, 9, 1636, 3869), ('CJQ', 26, 33, 3178, 2445)]
for code, r, c, x, y in tests:
    cx, cy = ring_canvas(r, c, x, y)
    px = im.getpixel((cx, cy))
    print(code, 'at', (cx, cy), 'px:', px, 'icon:', px != (8, 10, 16) and sum(px) > 60)
