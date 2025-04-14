'''
A calculator program that does following arthemetic calculations
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Truncated division
6. Modulus
7. Exponentiation
'''

#Function that does these calculations (also it has only two decimal place):
def add(a, b):
    print(f"Sum of {a} and {b} is {(a + b):.2f}")
def sub(a, b):
    print(f"Subtraction of {b} from {a} is {(a - b):.2f}")
def mul(a,b):
    print(f"Multiplication of {a} and {b} is {(a * b):.2f}")
def div(a,b):
    print(f"Division of {a} from {b} is {(a / b):.2f}")
def turdiv(a,b):
    print(f"Truncated division of {a} from {b} is {(a // b):.2f}")
def mod(a,b):
    print(f"Modulus of {a} from {b} is {(a % b):.2f}")
def expo(a,b):
    print(f"Exponentiation of {a} to the power of {b} is {pow(a,b):.2f}")

#A user view portal of calculator
def calculator():
    print("1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Division\n"
    "5. Truncated division\n"
    "6. Modulus\n"
    "7. Exponentiation\n"
    "To exit write any number\n")
    
    #Prompts user to input the choice
    n = int(input("Enter your choice: "))

    #Checks condition if falls below or above condtion program exits
    if n <= 0 or n >= 8:
        print("Exiting the program!!\n")
        exit(0)

    #Prompt user for decimal parameters
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    #Checks the condition
    if n == 1:
        add(a,b)
    elif n == 2:
        sub(a,b)
    elif n == 3:
        mul(a,b)
    elif n == 4:
        div(a,b)
    elif n == 5:
        turdiv(a,b)
    elif n == 6:
        mod(a,b)
    elif n == 7:
        expo(a,b)
    else:
        exit(0)

calculator()
