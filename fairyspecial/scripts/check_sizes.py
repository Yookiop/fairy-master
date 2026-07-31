import json, struct, sys
m = json.load(open('static/chunks/manifest.json'))
maxx = max(ch['bbox'][2] for ch in m['chunks'])
maxy = max(ch['bbox'][3] for ch in m['chunks'])
print('manifest expected size:', maxx, maxy)
with open('static/map_stitched.png','rb') as f:
    sig = f.read(8)
    # read chunks until IHDR
    chunk_len = f.read(4)
    chunk_type = f.read(4)
    if chunk_type != b'IHDR':
        # try to seek to IHDR
        f.seek(8)
        found = False
        while True:
            l = f.read(4)
            if not l: break
            t = f.read(4)
            if t == b'IHDR':
                found = True
                ihdr = f.read(8)
                w,h = struct.unpack('>II', ihdr)
                print('stitched size:', w, h)
                break
            # skip rest of chunk
            ln = struct.unpack('>I', l)[0]
            f.seek(ln + 4, 1)
        if not found:
            print('IHDR not found')
            sys.exit(1)
    else:
        ihdr = f.read(8)
        w,h = struct.unpack('>II', ihdr)
        print('stitched size:', w, h)
