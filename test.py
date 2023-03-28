import numpy as np

arr = np.zeros((3,3))
print(arr)

arr2 = np.ones((3,3))
print(arr2)

arr3 = np.arange(1,19)
print(arr3.reshape(6,-1))

arr4 = np.eye(4)

print("Identity Matrix of shape 4x4", arr4)
print(arr4.shape)

arr5 = np.array([[[1, 2, 3],
                 [2, 3, 4]],
                 [[3, 4, 5],
                 [4, 5, 6]]])

print(arr5)
print(arr5.ndim)
print(arr5.shape)