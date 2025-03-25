def prime(n):
    for i in range(2, n):
        if n % i == 0:
             return False
    return True

n = 44

if(prime(n)):
    print(f"The number {n} is prime")
else:
    print(f"The number {n} is not prime")