'''
Program for a simple guessing game.

Generating a random number and letting the user to guess the number

Checks if the number entered by the user is too low or too high and returns result

If the user enters the right number it prints You won

If the user exceed the given attempt which is 5 then program displays "Game Over"
'''

#importing random library
import random

#using randint to generate a random number from 1 to 100
a = random.randint(1, 100)

#initial value of i to be 1 just to print the attempt number in input section
i = 1

#while loop runs till the value of i is 6
while i != 6:

    #prompts the user for input
    b = int(input(f"\nGuess a number between(1 - 100) \nAttempt {i}/5: "))
    
    #checks if the input matches the result
    if b != a:
        if b > a:
            print("Too high")
        else:
            print("Too low")
        i += 1

    #checks if the input matches the result
    elif b == a:
        print("You won")
        break

#Prints this if the all attempt are used
if i == 6:
    print("\n\t\tGame Over")
        