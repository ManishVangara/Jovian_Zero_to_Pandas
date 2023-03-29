#1 Import the numpy package under the name np.
import numpy as np

#2 Print the numpy version and configuration
print(np.__version__)

#3 Create a null vector of size 10
null_vector_size10 = np.zeros((1,10))
print(null_vector_size10)
print(null_vector_size10.size)

#4 How to find the memory size of any array
memory_size = null_vector_size10.nbytes
print(memory_size)
memory_size2 = np.arange(1,91).nbytes
print(memory_size2)
    # Convert into Megabytes
print("Memory Size of 2nd array in MB", memory_size2/1024, "MB")

#5 How to get the documentation of the numpy add function from the command line?
    # Open command line and follow the code below
'''
python3 
import numpy as np
help(np.add)
'''

#6 Create a null vector of size 10 but the fifth value which is 1.
null_vector = np.zeros((10,1))
null_vector[4] = 1
print(null_vector)

#7 Create a vector with values ranging from 10 t0 49
arr = np.arange(10,50)
print(arr)
print(arr.size)
reshaped =arr.reshape((5,4,2))
print(reshaped)

#8 Reverse a vector (first element becomes last)
reversed = arr[::-1]
print(reversed)

#9 Create a 3x3 matrix with values ranging from 0 to 8
arr3x3 = np.arange(0,9).reshape((3,3))
print(arr3x3)

#10 Find indices of non-zero elements from [1,2,0,0,4,0]
arr2 = np.array([1,2,0,0,4,0])
result = np.where(arr2 != 0)[0]
print(result)
    # Other method
result2 = np.nonzero(arr2)
print(result2[0])

