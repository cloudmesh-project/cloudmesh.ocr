import numpy as np
from mnist import mnist_read
import cv2


mnist_path = '/home/saber/Courses/Semester_1/BigData/Dataset'

mnist_train = list(mnist_read(dataset='training', path=mnist_path))


"""
    Generating trainData and trainLabels from MNIST, for OpenCV KNearest()
    The data read form MNIST is supposed to be in a list, named mnist_list
"""

img_size = mnist_train[0][1].size
label_vec = np.zeros(len(mnist_train), dtype=np.float32)
flt_img_arr = np.zeros([len(mnist_train), img_size], dtype=np.float32)
for i in range(len(mnist_train)):
    label_vec[i] = mnist_train[i][0]
    flt_img_arr[i, :] = mnist_train[i][1].flatten()

#knn = cv2.ml.KNearest_create()
knn = cv2.KNearest()
knn.train(flt_img_arr, label_vec)

mnist_test = list(mnist_read(dataset='testing', path=mnist_path))
img_size_test = mnist_test[0][1].size
label_vec_test = np.zeros(len(mnist_test), dtype=np.float32)
flt_img_arr_test = np.zeros([len(mnist_test), img_size], dtype=np.float32)
for i in range(len(mnist_test)):
    label_vec_test[i] = mnist_test[i][0]
    flt_img_arr_test[i, :] = mnist_test[i][1].flatten()
    
ret,result,neighbours,dist = knn.find_nearest(flt_img_arr_test,k=5)  # Took 4:30
matches = (result.squeeze()==label_vec_test.squeeze())
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print accuracy