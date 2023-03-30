import numpy as np

#11 Create a 3X3 identity matrix
identity_matrix = np.eye(3, dtype='int64')
print(identity_matrix)
    #or
identity_matrix_2 = np.array([[1,0,0],
                              [0,1,0],
                              [0,0,1]])
print(identity_matrix_2)

#12 Create a 3x3x3 array with random values
arr_3x3x3 = np.random.rand(27).reshape((3,3,3))
print(arr_3x3x3)
print(arr_3x3x3.shape)
    #or
arr_3dim = np.random.rand(3,3,3)
print(arr_3dim)

#13 Create a 10x10 array with random values and find the minimum and maximum values
arr_10x10 = np.random.rand(10,10)
minimum = np.min(arr_10x10) #or you can call as methods --> arr_10x10.min()
maximum = np.max(arr_10x10)
print(f'Minimum -> {minimum}, Maximum -> {maximum}')

#14 Create a random vector of size 30 and find the mean value
vector_30 = np.random.rand(30)
mean_value = vector_30.mean()
median_value = np.median(vector_30)
print(mean_value)
print(median_value)

#15 Create a 2d array with 1 on the border and 0 inside
# Method 1 -> tedious Process
arr_2d = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]])

# Method 2 
arr_2dimensional = np.ones((5,5))
print(arr_2dimensional)
arr_2dimensional[1] = [1,0,0,0,1]
arr_2dimensional[2] = [1,0,0,0,1]
arr_2dimensional[3] = [1,0,0,0,1]
print(arr_2dimensional)

# Method 3 -> slicing and indexing
arr_5 = np.ones((10,10))

arr_5[1:-1,1:-1] = 0

print(arr_5)

#16 How to add a border (filled with 0's) around an existing array?
# Using slicing is the best option or we can manually update the values.

arr_existing = np.arange(1,31).reshape((6,-1))
print(arr_existing)
arr_existing[0,:] = 0
arr_existing[-1,:] = 0
arr_existing[:,0] = 0
arr_existing[:,-1] = 0
print(arr_existing)

#17 What is the result of the following expression?
'''
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
np.nan in set([np.nan])
0.3 == 3 * 0.1
'''

'''
# Multiply 0 by np.nan
print(0 * np.nan)   # Output: nan

# Check if np.nan is equal to np.nan
print(np.nan == np.nan)   # Output: False

# Check if np.inf is greater than np.nan
print(np.inf > np.nan)   # Output: False

# Subtract np.nan from np.nan
print(np.nan - np.nan)   # Output: nan

# Check if np.nan is in a set containing np.nan
print(np.nan in set([np.nan]))   # Output: True

# Compare 0.3 with 3 * 0.1
print(0.3 == 3 * 0.1)   # Output: False
Explanation:

When you multiply 0 by np.nan, the result is always np.nan, regardless of the value of the other operand.

NaN values are not equal to each other, and so np.nan == np.nan is False.

The expression np.inf > np.nan is False because any comparison involving NaN values always returns False.

Subtracting np.nan from np.nan results in np.nan, as the result is undefined.

The expression np.nan in set([np.nan]) is True, because the set constructor creates a set with a single element, which is np.nan.

The comparison 0.3 == 3 * 0.1 is False due to the way floating point numbers are represented in computers, which can lead to small rounding errors.

'''

#18 Create a 5x5 matrix with values 1,2,3,4 just below the diagonal.
arr_5x5 = np.zeros((5,5))
print(np.diag(arr_5x5))
np.fill_diagonal(arr_5x5[1:], [1,2,3,4])

print(arr_5x5)

# help(np.fill_diagonal)

print(arr_5)
np.fill_diagonal(arr_5[3:],[1,2,3,4,5,6,7])
print(arr_5)

#19 Create a 8x8 matrix and fill it with a checkboard pattern
checkboard = np.array([[0,1],
                       [1,0]])

arr_checkerboard = np.tile(checkboard,(4,4))
print(arr_checkerboard)

#20 Consider a (6,7,8) shape array, what is the index(x,y,z) of the 100th element.
arr_3 = np.zeros((6,7,8))

index = np.unravel_index(99,arr_3.shape)

print(index)