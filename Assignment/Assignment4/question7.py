import numpy as np
import random

arr = np.random.rand(1*10)
print(arr)

re_arr = arr.reshape(2, 5)
print(re_arr)

re_arr_ = arr.reshape(5, 2)
print(re_arr_)