'''
Program to let use populate two list and check following:
1. If the length of both list are same
2. If all element of both list adds up to same number
3. If any value from list1 occurs in list2
'''

#Initializing lists
list1 = []
list2 = []

#Function to get input for the list
def num_enter(n):
    while True:
        print(f"\nEntered numbers are {n}")
        #prompt user to input data and checks if user want to exit
        data = input("Enter a number ('quit' to exit): ")

        try:
            if data == 'quit':
                break

            number = int(data)
            n.append(number)
        except ValueError as v:
            print("Enter valid data")

#Function to check length of lists
def same_length(l1, l2):
    if len(l1) == len(l2):
        print("\nIt is of same length")
    else:
        print("\nThe both list are of different length")

#Function to check if both lists add upto same number
def same_value(l1, l2):
    res1 = 0
    res2 = 0

    #Adding all elements
    for i in l1:
        res1 += i

    for i in l2:
        res2 += i

    #Checking condition
    if res1 == res2:
        print("The sum of all elements of both list are same.")
    else:
        print("The sum of all elements of both list are not same.")

#Function to see if the value occurs in both list
def occur_value(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False
       

#Calling all the functions:
num_enter(list1)
num_enter(list2)

same_length(list1, list2)
same_value(list1, list2)
if occur_value(list1, list2):
    print("The value has occur in both list.")
else:
    print("It doesn't occur!")