'''
Program that calculates the number of digits and letters from the string entered by user

Using in loop to get all the char form the string
use if loop to check the char is either digit or letter using in-built function of python
'''

#Prompt user for input
a = str(input("Enter the targeted string: "))

#initializing the result value 
num = 0
letter = 0

#using loop to get the character from the string
for i in a:

    #check if the char is digit
    if i.isdigit():
        num += 1

    #check if the char is letter
    elif i.isalpha():
        letter += 1
    
print(f"The total number of numbers in string {a} is {num}")
print(f"The total number of letters in string {a} is {letter}")