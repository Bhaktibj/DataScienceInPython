""" What if we want to inspect the first three elements from the first row in a 2darray? We use ":"
to select all the elements from the index up to but not including the ending index. This is called slicing."""

from numerical_array import heights, ages, is_active, names
import numpy as np

heights_array = np.array(heights)
ages_array = np.array(ages)
ages_and_heights = heights + ages
ages_and_heights_array = np.array(ages_and_heights)
print("Index heights  is :", heights_array[0], heights_array[3])
print("Index ages is :", ages_array[0], ages_array[3])
reshape_array = ages_and_heights_array.reshape(2, 20)
print("2D array using index: ", reshape_array[1, 2])
print("2D array using slice: ", ages_and_heights_array[0:3])
# =================================================================
""" Assign the values"""
print("Before assign the value:", ages_and_heights_array)
ages_and_heights_array[0:2] = [190, 58]
print("After Assign the value", ages_and_heights_array)

# ==================================================================

""" update data in a subarray """

new_record = np.array([[180, 183, 190], [54, 50, 69]])
ages_and_heights_array = new_record
print(ages_and_heights_array)