import numpy as np

# arr = np.array([1,2,3])
# print(arr)
# print(type(arr))

#--------------------------------------------------------

# print(np.__version__)

#--------------------------------------------------------

# 0 dimentional array

# arr = np.array(43)          
# print(arr)

#--------------------------------------------------------

# 1 dimentional array

# arr = np.array([1,2,3])       
# print(arr)

#--------------------------------------------------------

# 2 dimentional array

# arr = np.array([[1,2,3],[4,5,6]])             
# print(arr)

#--------------------------------------------------------

# a fun 3x3 matrix

# arr = np.array([["a11","a12","a13"],["a21","a22","a23"],["a31","a32","a33"]])                 
# print(arr)

#--------------------------------------------------------

# 3 dimentional array

# arr= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])      
# print(arr)

#--------------------------------------------------------

# ndim : returns an integer that tells us how many dimensions the array have.

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

#--------------------------------------------------------

# When the array is created, you can define the number of dimensions by using the ndmin argument.

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

#--------------------------------------------------------

# accessing 1d arrays

# array_1d = np.array([1, 2, 3, 4])
# print(array_1d[0]+array_1d[3])

#--------------------------------------------------------

# accessing 2d arrays

# array_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', array_2d[0, 1])     
# print('3rd element on 2nd row: ',array_2d[1,2])
# print('3rd Last element on 2nd row: ',array_2d[1,-3])

#--------------------------------------------------------

# accessing 3d arrays

# array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(array_3d[1,0,1])        #gives 8
# print(array_3d[0,1,2])        #gives 6

#--------------------------------------------------------

# 1d array slice

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])         #gives 2,3,4,5
# print(arr[4:])          #gives 5,6,7
# print(arr[:4])          #gives 1,2,3,4
# print(arr[-3:-1])       #gives 5,6
# print(arr[0:6:2])       #gives 1,3,5
# print(arr[-1::-2])     #gives 7,5,3,1
# print(arr[-1::-1])     #gives 7,6,5,4,3,2,1
# print(arr[::1])         #gives 1,2,3,4,5,6,7
# print(arr[::2])         #gives 1,3,5,7
# print(arr[-1::-2])     #gives 7,5,3,1
# print(arr[-1::-1])     #gives 7,6,5,4,3,2,1
# print(arr[::1])         #gives 1,2,3,4,5,6,7
# print(arr[::2])         #gives 1,3,5,7

#--------------------------------------------------------

# 2d array slice

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])     #gives 2
print(arr[1,2])     #gives 8
print(arr[1,-3])    #gives 8

#--------------------------------------------------------
