import numpy as np

# To add two matrices.
a = np.array([[1,2,3] , [4,5,6]])
b = np.array([[1,2,3] , [4,5,6]])
sum = a+b
print(sum)

to_sum = np.array([[0 for i in range(0,len(a[0]))],[0 for i in range(0,len(b[0]))]])
print(to_sum)
print(len(a))

for i in range(0 , len(a-1)):
    for j in range(0 , len(b[0]-1)):
        to_sum[i][j] = a[i][j] + b[i][j]

print(to_sum)
