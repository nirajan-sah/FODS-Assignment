'''
program creating a vector of size 10
'''
import numpy as np

#using linspace and slicing first and last element i.e 0 and 1
vector = np.linspace(0,1,12)[1:-1]

print(vector)