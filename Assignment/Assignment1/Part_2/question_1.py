''' 
Program to take a number as input and display if it is even or odd
'''

#prompt user to input number
a = int(input("Enter a number: "))

#use statement if the number returns any remainder when divided by 2
if a % 2 == 0:

    #return this if the statement is true
    print(f"The number {a} is an even number.")
else:

    #return this if the statement is false
    print(f"The number {a} is an odd number")
