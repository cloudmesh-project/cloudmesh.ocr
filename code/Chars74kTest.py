#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:14:54 2017

@author: saber
"""
import numpy as np
import cv2
from ExtractChars74Kdataset import char74kdata
labels, allimages = char74kdata(100)

# Converting to numpy flattened arrays and separating into train and test
MIDDLE = np.uint(len(allimages) / 2)
train_labels = np.asarray(labels[0: MIDDLE], dtype=np.float32)
test_labels = np.asarray(labels[MIDDLE:len(labels)], dtype=np.float32)
train_images = np.zeros([MIDDLE, allimages[0].size], dtype=np.float32)
test_images = np.zeros_like(train_images)
for i in range(MIDDLE):
    train_images[i, :] = allimages[i].flatten()
    test_images[i, :] = allimages[np.uint(i+MIDDLE)].flatten()

knn = cv2.KNearest()
knn.train(train_images, train_labels)

ret,result,neighbours,dist = knn.find_nearest(test_images, k=5)  # Took 20seconds for n=50

matches = (result.squeeze()==test_labels.squeeze())
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
np.savetxt("test_labels.csv", result, delimiter=",")
np.savetxt("test_accuracy.txt", accuracy)

# Results:
    # n=50: 20 seconds to run => 65% accuracy
    # n=100: 80 seconds to run => 72% accuracy
    # n=150: 170 seconds to run => 72% accuracy
