'''
Program to calculate the simple interest with the data provides by user
The formula to calculate the simple interest is (principle * interest_rate * time_period)/100
'''

#prompt user 
principle = float(input("Enter the principle amount: "))
interest_rate = float(input("Enter the yearly rate of interest: "))
time_period = float(input("Enter the time period: "))

#Use formula to calculate
SI = (principle * interest_rate * time_period)/100

#print result
print(f"The simple interest of principle amount {principle} with interest rate of {interest_rate} for time period {time_period} is {SI} and the total amount is {SI + principle}")