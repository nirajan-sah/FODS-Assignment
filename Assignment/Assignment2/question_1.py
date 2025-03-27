'''
The program check how many Upper case and Lower case letters are there in a string.

The method is very simple 
At first using for in loop we seperate each char and check if the character is lower or upper and add to result.
'''

#Function to the program
def checkupperandlower():

    #prompt user for input
    a = str(input("Enter a String: "))
    
    #Initializing the value
    upper = 0
    lower = 0

    #loop to take one char at one time from string
    for i in a:

        #Condition if the char is upper
        if i.isupper():
            upper += 1
        else:
            lower += 1
    
    #Printing result
    print(f"The string {a} contain {upper} upper case and {lower} lower case letters")

#Calling the function
checkupperandlower()
