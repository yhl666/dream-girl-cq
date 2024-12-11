#ch4-29_ImageTransformationofPattern1
from PIL import Image
lena =Image.open("D:\ch4_demo\scene.jpg")
lena.show()
print(lena.mode)
print(lena.getpixel((0,0)))
lena_1 = lena.convert("1")
print(lena_1.mode)
print(lena_1.size)
print(lena_1.getpixel((0,0)))
print(lena_1.getpixel((10,10)))
lena_1.show()
