# without Numpy
from arrays import heights
count = 0
for height in heights:
    if height > heights[0]:
        count += 1
print("The total number of  heights is greater than heights[0]= ", count)  # validate
