'''
    Function to check if a given number is an Armstrong number.
    An Armstrong number (also known as a narcissistic number) is a number that is equal to 
    the sum of its own digits each raised to the power of the number of digits.
    
    Example:
    153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''

#Function to check armstrong
def armstrong():
    num = int(input("Enter a number to check: "))

    #Get the len of num
    n = len(str(num))

    #make a copy of num
    constnum = num
    result = 0

    #Run loop until the num is 0
    while(num != 0):

        #Get last value of nuum
        p = num % 10

        #raise last value with power of n
        result += pow(p, n)

        #remove the last value from num
        num = num//10
    
    #check armstrong
    if result != constnum:
        print(f"The number {constnum} is not an Armstrong number")
    else:
        print(f"The number {constnum} is an Armstrong number")

armstrong()
