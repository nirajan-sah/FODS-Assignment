with open("Origin.txt","r") as r, open("Dups.txt","w") as w:
    w.write(r.read())

r = open("Origin.txt")
print(f"1. The original text was: \n\n{r.read()}")

w = open("Dups.txt")
print(f"\n2. The Dublicate text was: \n\n{w.read()}")