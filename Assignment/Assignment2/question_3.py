def armstrong():
    num = int(input("Enter a number to check: "))
    n = len(str(num))
    constnum = num
    result = 0
    while(num != 0):
        p = num % 10
        result += pow(p, n)
        num = num//10
    
    if result != constnum:
        print(f"The number {constnum} is not an Armstrong number")
    else:
        print(f"The number {constnum} is an Armstrong number")

armstrong()
