''''
A program to calculate list of names and sort them
'''

#Function to sort names
def sortnames():

    '''
    Input names in this format: Nirajan,Samir,Anish,....
    '''
    names = str(input("Enter the number of names: "))

    #Will seperate the value from ,
    list_name = names.split(",")

    #using in-built sort function to sort names
    sortedname = sorted(list_name)

    #Printing the result
    print(sortedname)

sortnames()
    