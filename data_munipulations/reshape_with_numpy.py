from numerical_array import ages, heights
import numpy as np

""" Add the ages and heights of employees"""
ages_and_heights = heights + ages
ages_and_heights_array = np.array(ages_and_heights)
print("size of combined ages and heights array:", ages_and_heights_array.size)
print("shape of combined ages and heights array:\n", ages_and_heights_array.reshape(2, 20))  # created 2 rows with
