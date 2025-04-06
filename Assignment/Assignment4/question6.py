import numpy as np


def indexes(n):
    a = n[2:5]
    print(f"Element beween 2-5 is: {a}")

    a = n[5:8]
    print(f"Element beween 5-8 is: {a}")

    a = n[2:9]
    print(f"Element beween 2-9 is: {a}")



arr = []

while True:
    if len(arr) <= 9:
        a = int(input(f"Enter a number ({len(arr) + 1}): "))
        arr.append(a)
    else:
        a = input("Enter a number or end: ")
        if a == 'end':
            break
        try:
            arr.append(int(a))
        except Exception as e:
            print("An error as occured ", e)



indexes(n = np.array(arr))