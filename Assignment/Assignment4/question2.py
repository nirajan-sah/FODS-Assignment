'''
A program to generate user given shape of random array and finding the mean of array using numpy
'''

import numpy as np

#using a function
def array(a, b):

    #using inbuilt random function to get random numbers
    x = np.random.randn(a, b)
    
    #using inbuilt mean function to find average
    y = np.mean(x)

    print(f"\nThe given array is: \n{x}\n")
    print(f"The mean of array is: {y}")

#Prompt user for input
a = int(input("Enter Y-axis: "))
b = int(input("Enter the X-axis: "))

#Giving value to function
array(a, b)