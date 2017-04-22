#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:28:58 2017

@author: saber
"""
import numpy as np
import os.path as op
import cv2


def char74kdata(NUM_SAMPLES=1016):
    """This functions extracts images and their labels from Char74K Dataset.
    Input: Number of Sample fonts for each glyph (optional)
    Output: Images saved in a list
            and their corresponding labels in another list.
    Note that the compressed file must be already downloaded from the following
    URL and extracted in the parent directory:
    http://www.ee.surrey.ac.uk/CVSSP/demos/chars74k/EnglishFnt.tgz
    """

    NUM_GLYPHS = 62  # 0-9, A-Z, a-z
    # NUM_SAMPLES = 1016  # 1016 different fonts

    dir_path = op.dirname(op.realpath(__file__))
    dir_path_sep = op.split(dir_path)
    image_dir = op.join(dir_path_sep[0], 'English/Fnt')
    
    glyph_file_dir = []
    for i in range(1, NUM_GLYPHS+1):  # Because filenames start from 1
        glyph_file_dir.append("Sample%.3d" % i)
    
    labels_data = []
    image_data = []
    for i in range(1, NUM_GLYPHS+1):
        for j in range(1, NUM_SAMPLES+1):
            name_p1 = "img%.3d" % i
            name_p2 = "-%.5d" % j
            name_p3 = ".png"
            filepath = op.join(image_dir, glyph_file_dir[i-1], name_p1+name_p2+name_p3)
            image_data.append(cv2.imread(filepath, 0))
            labels_data.append(i-1)
    
    """
    Randomize the order of data
    """
    order = np.random.permutation(NUM_GLYPHS*NUM_SAMPLES)
    image_data_rand = []
    labels_data_rand = []
    for i in range(len(order)):
        image_data_rand.append(image_data[order[i]])
        labels_data_rand.append(labels_data[order[i]])
    
    # Deleting unnecessary variables to release memory
    del image_data
    del labels_data
    del glyph_file_dir
    return labels_data_rand, image_data_rand

"""
# Testing one of images for validity
import matplotlib.pyplot as plt
plt.imshow(image_data_rand[30000])
labels_data_rand[30000]
"""
