# Advantages -> We can use mulidimensional array as well.
# Importing all functions from array module

from numpy import *

values = array([12,23,4,5,56,76,'in']) # defining data-type is optional
print(values)


# Adding two arrays
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
arrSum = arr1 + arr2
print("Sum of the arrays are : " , arrSum)


# MultiDimensional Array
arrM = array([
                [1,2,3],
                [4,5,6]
            ])
print(arrM)

# Converting MultiDimensional Array into Matrix
matrixx = matrix(arrM)
print(matrixx)

# Matrix Multiplication
m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('11 22 33 ; 44 55 66 ; 77 88 99')
m3mult = m1 * m2
print(m3mult)