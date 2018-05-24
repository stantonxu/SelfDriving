import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


image = mpimg.imread('test.jpg')
print('This image is : ', type(image), 'with dimentions: ', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)

red_threshold = 200
green_threshold = 200
blue_threshold = 200
rgb_thredhold = [red_threshold, green_threshold, blue_threshold]

thresholds = (image[:,:,0] < rgb_thredhold[0]) | \
            (image[:,:,1] < rgb_thredhold[1]) | \
            (image[:,:,2] < rgb_thredhold[2])
color_select[thresholds] = [0,0,0]

plt.imshow(color_select)
plt.show()
