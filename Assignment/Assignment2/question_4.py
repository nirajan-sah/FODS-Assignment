def sortnames():
    names = str(input("Enter the number of names: "))
    list_name = names.split(",")
    sortedname = sorted(list_name)
    print(sortedname)

sortnames()
    