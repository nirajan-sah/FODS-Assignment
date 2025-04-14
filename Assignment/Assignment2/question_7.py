'''
Program that prompts user for names and store them in list and displayes how many a's are there in all the list
'''

#Initialize list
name = []
while True:
    #Prompt user for name if n == 0 program is turnicated
    n = str(input("Enter names and to exit '0': "))

    if n == '0':
        break

    #appending n in list
    name.append(n)

    #Initial value of a's is 0
    reuslt = 0

    #Get single name the list
    for ele in name:
        #Check all the character from the name if character is a then adds 1 to result
        for char in ele:
            #Lowering the character to get precise result
            if char.lower() == 'a':
                reuslt += 1

#Printing the result
print(f"{name}\n")
print(f"The total number of letter a in the list is {reuslt}\n")    