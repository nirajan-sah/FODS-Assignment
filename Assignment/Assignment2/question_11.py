dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#Code to concatenate all dictionaries
nums = {**dic1, **dic2, **dic3}
print(nums)

#Code to add the key and value to the dictionaries
nums[7] = 70
print(nums)

#Code to update the value of a key
nums[3] = 80
print(nums)

#Code to remove a item form dictionaries
del nums[3]
print(nums)

#Code to get sum of all item/value from dictionaries
value = 0
for key in nums.keys():
    value += nums[key]
print(value)

#Code to get multiply of all item/value from dictionaries
result = 1
for key in nums.keys():
    result *= nums[key]
print(result)

#Code to get maximum value
high = nums[1]
for key in nums.keys():
    if nums[key] > high:
        high = nums[key]
print(high)

#Code to get lowest value
low = nums[1]
for key in nums.keys():
    if nums[key] < low:
        low = nums[key]
print(low)