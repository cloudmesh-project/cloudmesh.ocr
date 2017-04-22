#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:51:22 2017
@author: saber

This function receives the file path of an image and returns a 3D list.
- The first dimension represents the lines of text.
- The second dimension is for words in each line.
- The third dimension represents the letters in each word. The elements in this
    dimension are numpy arrays, that can be visualized as an image and passed
    to a classifier.
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


def segment(image_path):
    
    # Reading the image file into an array.
    image_arr = cv2.imread(image_path, 0)
    if image_arr is None:
        raise ValueError, "Error reading file"
    
    FOREGND_THRESH = 100  # The intensities lower than this threshold are
    # considered as foreground. This is not very sensitive, in case Binarization
    # have been applied previously.
    H_THRESH = 4  # The rows having more foreground pixels than this number,
    # will be incorporated in a line. It might become invalid depending on the
    # length of line in text.
    V_THRESH = 1  # The columns having more foreground pixels than this number
    # will be incorporated in a letter. It might become invalid depending on the
    # amount of noise in the image and also its resolution.
    
    """ WORD_THRESH = 4: If there are this many consecutive background columns, 
    # a new word will be formed. This equals the minimum width of letters, as
    # calculated after letter segmentation.
    """
    
    """
     Line Detection using Projection Profile
    """
    v_idx = range(image_arr.shape[0])  # index to rows (vertical index)
    v_num = np.zeros(len(v_idx), dtype=np.uint8)  # number of black pixels in every row
    for i in v_idx:
        v_num[i] = sum(image_arr[i, :] < FOREGND_THRESH)
    
    i = 0
    sep_point = []
    while i in range(len(v_num)):
        if v_num[i] < H_THRESH:  # The row is in the background.
            pass
        else:
            up_bound = i  # Upper bound of a detected line
            try:
                while v_num[i] >= H_THRESH:  # passing all the rows incorporating the line
                    i += 1
                sep_point.append([up_bound, i])  # Add the upper and lower bound of
                # the line as a separation point.
            except IndexError:
                print "End of Page"
        i += 1
    
    """
    Line Segmentation
    """
    lines_list = []  # Contains the lines of the image as separated arrays.
    for i in range(0, len(sep_point)):
        starting_row = sep_point[i][0]
        ending_row = sep_point[i][1]
        lines_list.append(image_arr[starting_row:ending_row, :])
    
    """
    Letter and Word Segmentation
    """
    
    WORD_THRESH = 4
    
    forming_page = []
    for i in range(len(lines_list)):  # For every line, Do:
        cur_line = lines_list[i]  # cur_line contains grayscale intensities.
    
        h_idx = range(cur_line.shape[1])  # index to columns (horizontal index)
        f_num = np.zeros(len(h_idx), dtype=np.uint8)  # number of foreground pixels in every column
        for j in h_idx:  # Index to all columns in current line.
            f_num[j] = sum(cur_line[:, j] < FOREGND_THRESH)  # Counting the number
            # of foreground pixels in each column
        
        forming_line = []
        j = 0
        while j in h_idx:  # This loop processes one line and segments all the words inside.
            EOLetter = j  #     
            forming_word = []  # Starting to form a new word
            if f_num[j] > V_THRESH:
                while j - EOLetter < WORD_THRESH:    
                    # This block forms one word            
                    if f_num[j] > V_THRESH:
                        forming_letter = []  # Starting to form a new letter  
                        try:
                            while f_num[j] > V_THRESH:  # This block forms one letter
                                forming_letter.append(cur_line[:, j])
                                j += 1
                            EOLetter = j  # Marking the position of the end of current letter.
                            forming_word.append(np.transpose(np.asarray(forming_letter)))
                        except IndexError:
                            print "End of Line ", i
                    else:
                        j += 1
                forming_line.append(forming_word)
            else:
                j += 1
    
        if forming_line != []:
            forming_page.append(forming_line)

    return forming_page

"""
# Sample Usage
image_path = 'sample2.png'
forming_page = segment(image_path)

line = 1
word = 4
for i in range(len(forming_page[line][word])):
    plt.figure()
    plt.imshow(forming_page[line][word][i])
"""


