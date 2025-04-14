'''
A program to manupulate the dictionaries with each other and with itselfs
'''

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#Code to concatenate all dictionaries
nums = {**dic1, **dic2, **dic3}
print("The concatenating of all dictionaries is:",nums)

#Code to add the key and value to the dictionary
nums[7] = 70
print("Adding key 7 with value 70",nums)

#Code to update the value of a key
nums[3] = 80
print("Updating key 3 with value 80",nums)

#Code to remove a item form dictionary
del nums[3]
print("Deleting the key 3 from dictionary",nums)

#Code to get sum of all item/value from dictionary
value = 0
for key in nums.keys():
    value += nums[key]
print("The sum of all the value of keys is",value)

#Code to get multiply of all item/value from dictionary
result = 1
for key in nums.keys():
    result *= nums[key]
print("The multiplication of all the value of keys is",result)

#Code to get maximum value
high = nums[1]
for key in nums.keys():
    if nums[key] > high:
        high = nums[key]
print("The maximum value in dictionary is",high)

#Code to get lowest value
low = nums[1]
for key in nums.keys():
    if nums[key] < low:
        low = nums[key]
print("The minimum value in dictionary is",low)