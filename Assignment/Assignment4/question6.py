'''
program to conduct slicing in the number inputed by user
Question:
    Write a program to input an array of numbers from the user (at least 10 elements in list), 
    sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9.
'''
import numpy as np

#Using all kind of slicing given by question
def indexes(n):
    a = n[2:5]
    print(f"Element beween 2-5 is: {a}")

    a = n[5:8]
    print(f"Element beween 5-8 is: {a}")

    a = n[2:9]
    print(f"Element beween 2-9 is: {a}")


#initializing array
arr = []

while True:
    #Runs till the length of array is 9
    if len(arr) <= 9:
        a = int(input(f"Enter a number ({len(arr) + 1}): "))
        arr.append(a)
    #Runs after the length of array is greater than is 9
    else:
        a = input("Enter a number or 'end' to exit: ")
        if a == 'end':
            break
        #error handling is used if the user inputs other value is doesn't pollute the list
        try:
            arr.append(int(a))
        except Exception as e:
            print("An error as occured ", e)


#The array is changed into numpy array
indexes(n = np.array(arr))