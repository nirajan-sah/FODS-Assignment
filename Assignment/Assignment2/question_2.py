'''
Program to determine if the given number is prime for not

using to function 
is_prime() function which is bool type function which return true or false
prime() function which gets the condition form is_prime() and prints result accordingly
'''

#defining is_prime function
def is_prime(n):

    #checks if any number is perfectly dividing the given number
    for i in range(2, n):

        #Returns false if it is or true
        if n % i == 0:
             return False
    return True

#defining prime function
def prime(n):

    #if is_prime returns true then the number is prime else not prime
    if(is_prime(n)):
        print(f"The number {n} is prime")
    else:
        print(f"The number {n} is not prime")

#checking result
prime(1000003)
prime(1003)