from arrays import ages, heights
import numpy as np

ages_arr = np.array(ages)
heights_arr = np.array(heights)
height_age_arr = np.concatenate((heights_arr.reshape(1, 20), ages_arr.reshape(1, 20)),
                                axis=1)  # axis=1 means it is vertically combined
print("Vertically combined arrays using concatenate axis: ", height_age_arr)
# mathematical operations
print(height_age_arr[:, 0] * 2)  # 189*2
print(height_age_arr[:, 1] + 189)  # 189+189
print(height_age_arr[:, :2] * 2)  # [189*2], [170*2]
print(height_age_arr[:, 1] / 2)  # 170/2

# numpy array sum() method
print("Sum of combined arrays : ", height_age_arr.sum(axis=1))  # 2D Array is which computes sum axis=1
print("max of arrays", height_age_arr.max(axis=1))
print("min of arrays", height_age_arr.min(axis=1))
print("mean of arrays", height_age_arr.mean(axis=1))

# use axis=0
print("sum of height arrays horizontally: ", heights_arr.sum(axis=0))  # use single array
print("sum of ages arrays horizontally: ", ages_arr.sum(axis=0))  # use single array default axis is 0

# comparision of array
print("compare of the array: ", height_age_arr[:, : 2] < 55)  # returns boolean value
print("compare ages in the arrays: ", ages_arr[2] < 40)
print("compare array age: ", height_age_arr[:, :2] > 51)
print("compare array age: ", (height_age_arr[:, :2] > 51).sum())

# mask and subsettings
# first create mask
""" Masking is used to extract, modify, count, or otherwise manipulate values in an array based on some criterion. 
In our example, the criteria was height of 182cm or taller."""
mask = height_age_arr[:,0] >= 182
print("mask of sum is: ", mask.sum())

tallest_employee = height_age_arr[mask,]
print("mask employee is:", tallest_employee)
print("tallest employees shape is: ", tallest_employee.shape)
print("tallest employees array is: ", mask)

mask =(height_age_arr[:, 0]>=182) & (height_age_arr[:,1]<=50)
print("mask is:", mask)
print(height_age_arr[mask,])