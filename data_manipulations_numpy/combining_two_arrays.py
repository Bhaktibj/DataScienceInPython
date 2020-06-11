""" Combining The arrays """
""" To combine more than two arrays horizontally, simply add the additional arrays into the tuple """
from arrays import ages, heights
import numpy as np

# using hstack --- horizontal
ages_arr = np.array(ages)
heights_arr = np.array(heights)
heights_array = heights_arr.reshape((20, 1))  # 45 is first value in array
height_age_arr = np.hstack((heights_arr, ages_arr))  # using hstack
print("Combined horizontal arrays: ", height_age_arr)  # combined arrays
print("shape of arrays: ", height_age_arr.shape, "slice of the array: ", height_age_arr[:3, ])

# using vstack --- vertical combined arrays by vertically
heights_array_vertical = heights_arr.reshape((1, 20))
ages_array_vertical = ages_arr.reshape((1, 20))
height_age_arr = np.vstack((heights_arr, ages_arr))
print("Combined vertical arrays: ", height_age_arr)  # vertically combined arrays
print("shape of vertical combined arrays: ", height_age_arr.shape, "slice of the arrays: ", height_age_arr[:, :3])

# concatenate the arrays using to combined the two arrays - numpy.concatenate
height_age_arr = np.concatenate((heights_arr, ages_arr), axis=0)  # axis=0 means it is horizontally combined
print("Horizontally combined arrays using concatenate axis: ", height_age_arr)
height_age_arr = np.concatenate((heights_arr.reshape(1, 20), ages_arr.reshape(1, 20)),
                                axis=1)  # axis=1 means it is vertically combined
print("Vertically combined arrays using concatenate axis: ", height_age_arr)

