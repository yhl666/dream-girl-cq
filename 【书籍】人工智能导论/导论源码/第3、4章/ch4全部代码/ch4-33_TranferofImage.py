#ch4-33_TranferofImage
from PIL import Image
from pylab import *
im=Image.open("d:\\ch4_demo\scene.jpg")
out = im.resize((128, 128))     
out.show()
out = im.rotate(45)   
out.show()
out = im.transpose(Image.FLIP_LEFT_RIGHT)  
out.show()
out = im.transpose(Image.FLIP_TOP_BOTTOM)  
out.show()