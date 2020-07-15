# Limitation -> We can't use multidimensional array

# Importing all functions from array module

from array import *
values = array('i', [1,2,3,4,5,6,7])
print(values)
print(len(values)) # Length of an array

values.append(34) # Add element to an array
print(values)

for i in values:  # Printing array values
    print(i , end=" ")