""" Attribute size in numpy is similar to the built-in method len in python that is
 used to compute the length of iterable python objects like str, list, dict, etc. """

from arrays import heights, ages
import numpy as np

heights_array = np.array(heights)
print("Numpy n-dimensional array: ", heights_array)
print("Size of numpy array is: ", heights_array.size)  # find the size of array
print("Shape of numpy array is: ", heights_array.shape)  # find the dimension of array

