def checkupperandlower():
    a = str(input("Enter a String: "))
    upper = 0
    lower = 0
    for i in a:
        if i.isupper():
            upper += 1
        else:
            lower += 1

    print(f"The string {a} contain {upper} upper case and {lower} lower case letters")

checkupperandlower()
