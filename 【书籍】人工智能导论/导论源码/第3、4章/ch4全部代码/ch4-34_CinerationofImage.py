#ch4-34_CinerationofImage
from PIL import Image
from pylab import *
im=Image.open("d:\\ch4_demo\scene.jpg")
im.show()
from PIL import Image
from pylab import *
im = array(Image.open("d:\\ch4_demo\scene.jpg").convert('L'))
im2 = 255 - im 
im3 = (100.0/255) * im + 100   
im4 = 255.0 * (im/255.0)**2
subplot(221)
title('f(x) = x')
gray()
imshow(im) 
subplot(222)
title('f(x) = 255 - x')
gray()
imshow(im2)
subplot(223)
title('f(x) = (100/255)*x + 100')
gray()
imshow(im3)
subplot(224)
title('f(x) =255 *(x/255)^2')
gray()
imshow(im4)
print(int(im.min()),int(im.max()))
print(int(im2.min()),int(im2.max()))
print(int(im3.min()),int(im3.max()))
print(int(im4.min()),int(im4.max()))
show()
