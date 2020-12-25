import numpy as np

# To multiply two matrices.
A = np.array([[3, 6, 7], [5, -3, 0]])
B = np.array([[1, 1], [2, 1], [3, -3]])
mul = A.dot(B)
print(mul)
to_mul = np.array([[0 for i in range(0,len(A))],[0 for i in range(0,len(A))]])
print(to_mul)
print(A[0])
print(len(B[0]))
# 3, 6, 7      1 , 1
# 5,-3, 0      2 , 1
#              3 ,-3

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            to_mul[i][j] += A[i][k] * B[k][j]

print(to_mul)

