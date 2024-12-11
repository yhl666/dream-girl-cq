#ch4-35_AdjustPixelofImage
from PIL import Image
im=Image.open("d:\ch4_demo\scene.jpg")
im.show()
w,h=im.size
print(w)
print(h)
out = im.resize((800,800),Image.ANTIALIAS)
out.show()
w1,h1=out.size
print(w1)
print(h1)