from PIL import Image
from numpy import asarray
img = Image.open('gengar.jpg')
# load the image and convert into 
# numpy array
 
numpydata = asarray(img)
# data
print(numpydata)