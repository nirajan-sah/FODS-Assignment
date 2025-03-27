'''
    Function to check if a given number is an Armstrong number.
    An Armstrong number (also known as a narcissistic number) is a number that is equal to 
    the sum of its own digits each raised to the power of the number of digits.
    
    Example:
    153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
'''

def armstrong():
    num = int(input("Enter a number to check: "))
    n = len(str(num))
    constnum = num
    result = 0
    while(num != 0):
        p = num % 10
        result += pow(p, n)
        num = num//10
    
    if result != constnum:
        print(f"The number {constnum} is not an Armstrong number")
    else:
        print(f"The number {constnum} is an Armstrong number")

armstrong()
