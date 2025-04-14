'''
The program that prompts user to input value form 1 - 100 and store them in list and print them at last.
To finish the program user should write "finish" which is not case-sensative.
'''

#defining list
num = []

#Message for user
print("Enter numbers between 1 and 100 (type 'finish' to end):\n")

#Loops runs when all statements are true
while True:
    #prompts user for input
    in_num = input("Enter a number: ")
    
    #checks if user want to end program
    if in_num.lower() == 'finish':  
        break
    
    #Error exception method
    try:
        #Convert str in_num to int number
        number = int(in_num) 

        #Checks if the number is above 1 and below 100
        #And append if true to the list
        if 1 <= number <= 100: 
            num.append(number)

        #Else prints message saying number should be beween 1 - 100
        else:
            print("Number should be in between 1 to 100")
        
    #Checks if in_num can be converted into int if not displays this
    except ValueError:
        print("Invalid input! Enter number.")

print("\n\nThe entered numbers are: ", num, "\n")

