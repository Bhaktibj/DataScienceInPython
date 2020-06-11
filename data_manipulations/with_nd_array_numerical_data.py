from arrays import heights, ages
""" Find the heights greater than > 189 """
# using Numpy lib
import numpy as np

height_array = np.array(heights)  # create the numpy array using np.array
print("The total number of  heights is greater than heights[0]= ",(height_array > heights[0]).sum())  # validate

""" Add the ages and heights of employees """
ages_and_heights = heights + ages
ages_and_heights_array = np.array(ages_and_heights)
print(ages_and_heights_array)