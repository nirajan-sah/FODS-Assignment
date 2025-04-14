'''
program that creates 5 * 5 matrix whose value range form 0 - 4
using numpy and random library to build program
'''
import numpy as np

'''The value range from 0-4
reason to write 0,5 is because last number is exclusive'''
matrix = np.random.randint(0,5, size=(5,5))

print(matrix)