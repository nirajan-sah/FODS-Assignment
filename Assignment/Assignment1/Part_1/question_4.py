'''
Using single literation to calcualte factorial
The loop start form 1 and continues to the n + 1 value of number
'''

#Defining a fuction to calculate factorial of a given number as a variable in the form of value
def factorial(value):
    #Making a constant value     
    result = 1

    for i in range(1, value + 1):
        result *= i

    #Returning the result 
    return result

seven = factorial(7)
five = factorial(5)

print(f"The value of 7! - 5! is {seven - five}")