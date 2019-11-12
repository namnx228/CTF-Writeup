from PIL import Image

import random
import sys

def qq(x, y):
    return (2 * x + 3 * y + 29) % 256

def transform(pixelinfo):
    pixelreverse = [pixelinfo[len(pixelinfo)-1-i] for i in range(len(pixelinfo))]
    out = [pixelinfo[i] for i in range(len(pixelinfo))]
    for i in range(len(pixelinfo)):
        out[0] = qq(pixelreverse[i], out[0])
        for j in range(1,len(pixelinfo)):
            out[j] = qq(out[j-1], out[j])
    return out


image = Image.open(sys.argv[1])
outfile1 = Image.new(image.mode, image.size)

# for x in range(0, image.size[0]):
#     for y in range(0, image.size[1]):
#         sourcepixel = list(image.getpixel((x, y)))
#         print sourcepixel
#         tran = transform(sourcepixel)
#         outfile1.putpixel((x, y), tuple(tran))

listReverse=[[]]*256*256*256
hundred=256*256
ten=256

for x in range(0, 256):
    for y in range(0, 256):
        for z in range(0, 256):
            sourcepixel = [x,y,z]
            tran = transform(sourcepixel)
            listReverse[tran[0]*hundred+tran[1]*ten+tran[2]]=sourcepixel

for x in range(0, image.size[0]):
    for y in range(0, image.size[1]):
        sourcepixel = list(image.getpixel((x, y)))
        tran = listReverse[sourcepixel[0]*hundred + sourcepixel[1]*ten+sourcepixel[2]]
        outfile1.putpixel((x, y), tuple(tran))


outfile1.save('out1.bmp')
