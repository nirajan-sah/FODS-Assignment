'''
Program to find the number multiple of 5 and divisible by 7

At first the loop filters the number which are multiple of 5

The second if statement check the filtered number is divisible by 7 or not if it is divisible then prints the number else just pass the statement.
'''

for i in range(1500, 2001, 5):
    if i % 7 == 0:
        print(i)
    else:
        pass
