#import sys
import cv2
import numpy as np

def denoise_median(image_arr):
    # Mode Filter
    img_denoised = 255*np.ones_like(image_arr)
    for i in range(1, image_arr.shape[0]-2):
        for j in range(1, image_arr.shape[1]-1):
            block = image_arr[i-1:i+2, j-1:j+2]
            #img_denoised[i, j] = stats.mode(block.flatten())[0][0]
            img_denoised[i, j] = max(set(block.flatten()), key=list(block.flatten()).count)
    return img_denoised

"""
#Test Case
from matplotlib import pyplot as plt
image_arr = cv2.imread('sample9.png')

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
"""

def denoise_gaussian(image_arr):    
    # GaussianBlur

    # DELAY_BLUR = 500;
    for i in xrange(1, 31, 2):
        gaussian_blur = cv2.GaussianBlur(image_arr, (i, i), 0)
    return gaussian_blur
#        string = 'guassian_blur : kernel size - '+str(i)
#        cv2.putText(gaussian_blur, string, (20, 20),
#                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (123, 123, 123))
#        cv2.imshow('Blur', gaussian_blur)
#        cv2.waitKey(DELAY_BLUR)
