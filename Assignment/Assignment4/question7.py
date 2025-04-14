'''
creating a random matrix of 1 row and 10 column
and reshaping it into different types
'''
import numpy as np

#Creating a random matrix
arr = np.random.rand(1*10)
print("The 1 * 10 matrix is ",arr)

#Reshaping it into 2 rows and 5 columns
re_arr = arr.reshape(2, 5)
print("The 2 * 5 matrix is ",re_arr)

#Reshaping it into 5 rows and 2 columns
re_arr_ = arr.reshape(5, 2)
print("The 5 * 2 matrix is ",re_arr_)