import numpy as np


# <<<Create numpy array
# variable = np.array([2, 4, 5], dtype='float')
#
#
# print(type(variable))
#
# print(np.zeros((3, 5), dtype='int'))
#
# print(np.ones((3, 5), dtype='int'))
#
# print(np.full(8, 5))
#
# print(np.full((2, 3), 6))
#
# print(np.arange(5))
#
# print(np.arange(3, 10))
#
# print(np.eye(2, 3, dtype='int'))
#
# print(np.linspace(10, 30, 10))
#
# print(np.random.rand(5))
#
# print(np.random.rand(2, 3))
#
# print(np.random.randn(5))
#
# print(np.random.normal(20, 5, (4, 3)))
#
# print(np.random.randint(0, 10, (4, 4)))
#

# <<<numpy libraries
# <<reshape
# variable = np.arange(1, 16)
# print(variable)
# print(variable.ndim) #give dimention of array
#
# variable = variable.reshape((3, 5))
# print(variable)
# print(variable.ndim)
#
# variable = variable.reshape((1, 15))
# print(variable)
# print(variable.ndim)


# <<find max in array
# variable = np.random.randint(0, 15, 10)
# print(variable)
# print(variable.max())  # give max no
# print(variable.argmax())  # give index of max no
#
# array = np.random.randint(0, 50, (2, 3))
# print(array)
# print(array.max())
# print(array.argmax())

# <<find min in array
# array = np.random.randint(0, 10, 15)
# print(array)
# print(array.min())
# print(array.argmin())
# find min in 2 dimention as above in max


# <<concating two arrays
# array size must be same in both the array
# array = np.random.randint(0, 10, 15)
# array2 = np.random.randint(11, 20, 15)
#
# print(array)
# print(array2)
#
# array3 = np.concatenate([array, array2])
# print(array3)
#
# array = np.arange(1, 16).reshape(3, 5)
# print(array)
#
# array2 = array2.reshape(3, 5)
# print(array2)
#
# array3 = np.concatenate([array, array2])
# print(array3)
#
# array3 = np.concatenate([array, array2], axis=1)
# print(array3)


# <<split one dimentional array
# array = np.random.randint(0, 15, 10)
# print(array)
#
# array2 = np.split(array, [3, 5])
# print(array2)
#
# w, x, y, z = np.split(array, [3, 5, 7])
# print(w)
# print(x)
# print(y)
# print(z)
#
# array2 = np.split(array, 5) #Devide into equal parts
# print(array2)


# <<split two dimentional array
# array = np.arange(20).reshape(5, 4)
# print(array)
#
# array2 = np.split(array, [1, 3])
# print(array2)
#
# array3 = np.split(array, [1, 3], axis=1)
# print(array3)
#
# array4 = np.hsplit(array, 4)
# print(array4)
#
# array5 = np.hsplit(array, [1, 3])
# print(array5)
#
# array6 = np.vsplit(array, 5)
# print(array6)
#
# array7 = np.vsplit(array, [1, 3])
# print(array7)


# <<sort of array
# array = np.random.randint(0, 15, 10)
# print(array)
#
# array2 = np.sort(array)
# print(array2)
#
# array3 = array.reshape(2, 5)
# print(array3)
# array4 = np.sort(array3)
# print(array4)
#
# array5 = np.sort(array3, axis=0)
# print(array5)


# indexing numpy array
# array = np.random.randint(0, 11, 15)
# print(array)
# print(array[4])
# print(array[-2])
#
# array2 = np.array([[5, 10, 15,],
#                    [20, 25, 30],
#                    [33, 40, 45]])
# print(array2)
# print(array2[0, 1])
# print(array2[-1, -3])


# slicing of one dimentional array
# array = np.random.randint(0, 20, 15)
# print(array)
#
# array2 = array[2:5]
# print(array2)
#
# array3 = array[2:13:3]
# print(array3)
#
# array4 = array[:7:3]
# print(array4)


# slicing of two dimentional array
# array = np.random.randint(0, 30, 20).reshape(5, 4)
# print(array)
#
# array2 = array[2]
# print(array2)
#
# array3 = array[2, 2:4]
# print(array3)
#
# array4 = array[:,2]
# print(array4)
#
# array5 = array[2:4,2:4]
# print(array5)


# Assigning value to one dimentional array
# array = np.random.randint(0, 20, 15)
# print(array)
# 
# array[7] = 25
# print(array)
# 
# array[5:10] = 30
# print(array)
# it same in two dimentional array also


# fancy indexing in one dimentional array
# array = np.random.randint(0, 20, 15)
# print(array)
# 
# indexes = [1, 3, 7]
# print(array[indexes])
# same in two dimentional array


# Operationa with numpy array
# array = np.random.randint(0, 10, 15)
# print(array)
# 
# print(array > 5)
# 
# array2 = array[array > 5]
# print(array2)


# arithmetic operation in numpy array
# array = np.random.randint(0, 10, 15)
# print(array)
# 
# print(array - 2)
# print(array * 2)
# print(array*array)
# print(np.add(array, 2))
# print(np.divide(array, 2))
# print(array ** 3) # do exponent
# print(np.sqrt(4))
# print(np.sqrt(array))
# and many more mathematical operation


# statics in nmpy 
# array = np.random.randint(0, 10 , 15)
# print(array)
# 
# print(np.sum(array))
# print(np.mean(array))
# print(np.median(array))
# print(np.std(array))


# solve degree equation in nmpy library
# print("2x1 + x2 = 5\n-3x1 + 6x2 = 0")
# 
# coefficient = np.array([[2, 1], 
#                        [-3, 6]])
# print(coefficient)
# output = np.array([5, 0])
# print(output)
# 
# print(np.linalg.solve(coefficient, output))


