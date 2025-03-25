list1 = []
list2 = []

def numenter(n):
    while True:
        print(f"\nEntered numbers are {n}")
        data = input("Enter a number ('quit' to exit): ")

        if data == 'quit':
            break

        number = int(data)
        n.append(number)

def samelength(l1, l2):
    if len(l1) == len(l2):
        print("\nIt is of same length")
    else:
        print("\nThe both list are of different length")

def samevalue(l1, l2):
    res1 = 0
    res2 = 0
    for i in range(len(l1)):
        res1 += l1[i]

    for j in range(len(l2)):
        res2 += l2[j]

    if res1 == res2:
        print("The sum of all elements of both list are same.")
    else:
        print("The sum of all elements of both list are not same.")

def occurvalue(l1, l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[i]:
                return True
    return False
       


numenter(list1)
numenter(list2)

samelength(list1, list2)
samevalue(list1, list2)
if occurvalue(list1, list2):
    print("It occurs!")
else:
    print("It doesn't occur")