#ch4-30_ImageformationofPatternL
from PIL import Image
lena =Image.open("D:\ch4_demo\scene.jpg")
lena.show()
print(lena.mode)
print(lena.getpixel((0,0)))
lena_i = lena.convert("I")
print(lena_i.mode)
print(lena_i.size)
print(lena_i.getpixel((0,0)))
lena_i.show()
