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


def segment(image_arr):

    # Reading the image file into an array.
    # image_arr = cv2.imread(image_path, 0)
    if image_arr is None:
        raise ValueError, "Error reading file"

    FOREGND_THRESH = 100  # The intensities lower than this threshold are
    # considered as foreground. This is not very sensitive, in case Binarization
    # have been applied previously.
    H_THRESH = 2  # The rows having more foreground pixels than this number,
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

    WORD_THRESH = 14

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
                while (j - EOLetter < WORD_THRESH): #& (j in h_idx):
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
import matplotlib.pyplot as plt
image_path = 'sample2.png'
forming_page = segment(image_path)

line = 1
word = 4
for i in range(len(forming_page[line][word])):
    plt.figure()
    plt.imshow(forming_page[line][word][i])
"""


def line2arr(line):
    """
    This function receives a 2D list (line), created by segment() function.
    and returns an array that in each row, has the image of one letter
    flattened to a vector.
    Its result can be the input to knn.find_nearest()
    """
    
    if type(line[0][0]) != np.ndarray:
        raise ValueError, "Invalid input"
    else:
        letters = []
        for word in line:
            for letter in word:
                letter_reshaped = reshape2temp(letter)  # Resize image to the
                # shape of template.
                letters.append(letter_reshaped.flatten())
    let_size = 16384
    for i, letter in enumerate(letters):
        if letter.size < let_size:
            letters[i] = np.lib.pad(letter, (0, let_size-letter.size),
                                    'constant', constant_values=(255))
    """
    let_size = 0
    for letter in letters:
       if letter.size > let_size:
            let_size = letter.size
    
    for i, letter in enumerate(letters):
        if letter.size < let_size:
            letters[i] = np.lib.pad(letter, (0, let_size-letter.size), 'constant',
                                    constant_values=(255))
    """
    return np.asarray(letters, dtype=np.float32)
    #return letters


def reshape2temp(im1, new_size=16384):
    
    # Add padding
    pad_len = int(0.2*im1.shape[0])
    im1 = np.lib.pad(im1, ((pad_len, pad_len),(pad_len, pad_len)), 'constant', constant_values=255)
    ratio = np.sqrt(new_size/im1.size)
    new_nrow = int(np.floor(ratio * im1.shape[0]))
    new_ncol = int(np.floor(ratio * im1.shape[1]))
    return cv2.resize(im1, (new_ncol, new_nrow))  # This function oddly takes (col, row).
    #return new_ncol


if __name__ == "__main__":
    #import matplotlib.pyplot as plt
    image_path = 'sample3.jpg'
    image_arr = cv2.imread(image_path, 0)
    forming_page = segment(image_arr)
    letter_arr = line2arr(forming_page[1])
    new_im = reshape2temp(forming_page[0][1][0])
    