import numpy as np
#21 Create a checkerboard 8x8 matrix using the tile() function.
checker_pattern = np.array([[0,1],
                            [1,0]])

checkerboard = np.tile(checker_pattern,(4,4))
print(checkerboard)

#22 Create a checkerboard 8x8 matrix
checkboard = np.zeros((8,8),dtype=int)
print(checkboard)

checkboard[1::2,0:-1:2] = 1
checkboard[0::2,1::2]=1
print(checkboard)

    ##Checking
print(checkerboard==checkboard)

#22 Normalize a 5x5 random matrix
arr = np.random.rand(5,5)

mean = np.mean(arr)
std = np.std(arr)

    #Normalize the matrix
normalized_arr = (arr-mean)/std

print(normalized_arr)

#23 Create a custom dtype that describes a color as four unsigned bytes(RGBA)
'''
To create a custom dtype that describes a color as 
four unsigned bytes (RGBA), you can use the np.dtype() 
function with the ('name', 'format') syntax. Here's how:
'''
color_dtype = np.dtype([('r', np.ubyte),
                        ('g',np.ubyte),
                        ('b', np.ubyte),
                        ('a', np.ubyte)])

    # Search in Jobot

#24 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [10,11,12],
              [13,14,15]])

B = np.array([[1,2],
              [3,4],
              [5,6]])

print(np.dot(A,B))
print(np.matmul(A, B))

#25 Given a 1D array, negate all elements which are between 3 and 8, in place.
arr2 = np.array([1,2,3,4,5,6,7,8,9,10])

arr2[(arr2 >= 3) & (arr2<=8)] *= -1
print(arr2)


#26 What is the output of the following script?
    # Author: Jake VanderPlas
print(sum(range(5), -1))
from numpy import *
print(sum(range(5), -1))

'''
The Output: 9
            10

Here's why:

The first sum() function computes the sum of the range from 0 to 4 (sum(range(5))), and adds -1 to the final result. The result is therefore 9.

The second sum() function is imported from NumPy and behaves differently. It computes the sum of the range from 0 to 4 along the last axis (-1), which is the only axis in this case. The result is therefore the same as the first sum() function.

Note that the second sum() function is imported from NumPy using the from numpy import * statement, which is generally not recommended as it can lead to namespace collisions and other issues. It's better to import only the necessary functions from NumPy using import numpy as np and then prefixing the function calls with np.
'''
#27 Consider an integer vector Z, which of these expressions are legal?
'''
Z ** Z
2 << Z >> 2
Z <- Z
1j * Z
Z/1/1
Z<Z>Z
'''
Z = np.arange(1,10)
print(Z)

