#ch4-32_ExtractSizeofImage
from PIL import Image
from pylab import *
im=Image.open("d:\\ch4_demo\scene.jpg")
im.show()
box=(500,500,700,700)
region=im.crop(box)
region.show()
region=region.transpose(Image.ROTATE_180)
region.show()
im.paste(region,box)
im.show()


