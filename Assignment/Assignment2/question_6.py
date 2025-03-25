num = []

print("Enter numbers between 1 and 100 (type 'finish' to end):\n")

while True:
    in_num = input("Enter a number: ")
    
    if in_num.lower() == 'finish':  
        break
    
    try:
        number = int(in_num)  
        if 1 <= number <= 100: 
            num.append(number)
        else:
            print("Number should be in between 0 to 100")
    except ValueError:
        print("Invalid input! Enter number.")

print("\n\nThe entered numbers are: ", num, "\n")

