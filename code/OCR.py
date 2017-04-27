#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:01:07 2017

@author: saber
"""

import numpy as np
import cv2
from ExtractChars74Kdataset import char74kdata, label2char
from Binarization import binarize_otsu
from Denoising import denoise_median
from Segment import segment, line2arr
import matplotlib.pyplot as plt


def ocr(image_arr):
    """
    This function receives the url
    """
    
    knn = cv2.KNearest()
    """
    Training the KNN using Chars74k datatset.
    """
    
    # Load the train data.
    ch74_labels, ch74_images = char74kdata()
    
    # Convert to numpy array form and flatten the images.
    train_labels = np.asarray(ch74_labels, dtype=np.float32)
    train_images = np.zeros([len(ch74_images), ch74_images[0].size], dtype=np.float32)
    for i in range(len(ch74_images)):
        train_images[i, :] = ch74_images[i].flatten()
    
    # Train
    knn.train(train_images, train_labels)
    del ch74_images
    
    """
    Running recognition session on a sample image.
    """
    
    #image_path = 'sample9.png'
    #image_arr = cv2.imread(image_path, 0)
    #plt.imshow(image_arr)
    # Denoising
    image_denoised = denoise_median(image_arr)
    #plt.figure(); plt.imshow(image_denoised)
    
    image_bin = binarize_otsu(image_denoised)
    #plt.figure(); plt.imshow(image_bin)
    
    del image_arr, image_denoised
    
    forming_page = segment(image_bin)
    
    result=[]
    for i, line in enumerate(forming_page):
        letter_arr = line2arr(line)
        ret, resulting_labels, neighbours, dist = knn.find_nearest(letter_arr, k=31)
        line_text = [label2char(lbl) for lbl in resulting_labels]
        result.append(line_text)
    np.savetxt('OCRresult.txt', result, fmt='%s')

## For examining the neighbours as well.
#neigh_char = np.empty_like(neighbours, dtype=str)
#for i in range(neigh_char.shape[0]):
#    for j in range(neigh_char.shape[1]):
#        neigh_char[i][j] = label2char(int(neighbours[i][j]))

if __name__ == "__main__":
    import sys
    from PIL import Image
    import urllib, cStringIO
    image_url = sys.argv[1]
    #image_url="https://arturshams.files.wordpress.com/2015/07/sample2.png"
    myfile = cStringIO.StringIO(urllib.urlopen(image_url).read())
    img = np.array(Image.open(myfile))
    ocr(img)
