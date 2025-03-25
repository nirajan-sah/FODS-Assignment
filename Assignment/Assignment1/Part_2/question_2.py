'''
program to prompt the user to input two number 
and first number to be divided by second number with exactly two decimal places
'''

#prompt user to input the numbers
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))

#print the result
print(f"The result of dividing {a} by {b} is {round(a/b, 2)}")