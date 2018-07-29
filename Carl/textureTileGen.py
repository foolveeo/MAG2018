import cv2
import numpy as np
import matplotlib.pyplot as plt

black = np.zeros((5000,5000,3), np.uint8)
white = 255 * np.ones((5000,5000,3), np.uint8)
gray = 128 *  np.ones((10000,3000, 3), np.uint8)
composed = np.zeros((10000,8000,3), np.uint8)


zero = np.zeros((3), np.uint8)
one = 255 * np.ones((3), np.uint8)


for i in range(5000):    
    for j in range(5000):
        
        if(i < 100 or i > 4900 or (i < 2550 and i > 2450) or (i > 1200 and i < 1300) or (i > 3700 and i < 3800)):
            black[j,i] = one
            white[j,i] = zero
            
            
composed[0:5000, 0:5000,:] = black
composed[ 5000:10000,0:5000,:] = white
composed[:,5000:8000, :] = gray
plt.figure()      
plt.imshow(composed)

cv2.imwrite("/Users/fulvio/furvio/MAG/Carl/Textures/stripes.png", composed)
#cv2.imwrite("/Users/fulvio/furvio/MAG/Carl/Textures/white.png", white)

