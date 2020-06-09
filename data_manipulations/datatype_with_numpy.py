""" Numpy supports several data types such as int (integer), float (numeric floating point),
 and bool (boolean values, True and False)."""
# Note: numpy array is homogenious array
from numerical_array import heights, ages, is_active, names
import numpy as np

heights_array = np.array(heights)
ages_array = np.array(ages)
print("data type of heights_array is: ", heights_array.dtype)
print("data type of ages_array is: ", ages_array.dtype)
is_active_array = np.array(is_active)
print("data type of bool array is: ", is_active_array.dtype)
names_array = np.array(names)
print("data type of String array is: ", names_array.dtype)





