import numpy as np

a = [
        [11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]
    ]
A = np.array(a)
'''
print(A.ndim)
print(A.shape)
print(A.size)
'''
# transposed matrix
B = A.T
print(B)
print(B[0][1])
