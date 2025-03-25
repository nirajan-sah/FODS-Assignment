'''
Program to convert Celsius to Fahrenheit
The formula to convert in fahrenheit is (celsius * 9/5) + 32
'''

#prompt user to input the temperature in celsius
celsius = float(input("Enter the temperatur in celsius"))

#converting to the fahrenheit
fahrenheit = (celsius * 9/5) + 32

#printing result
print(f"The temperature {celsius} celcius in fahrenheit is {fahrenheit}")