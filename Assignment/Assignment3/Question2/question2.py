'''
program to copy content to new file
'''

#Opening orign.txt in read and dups.txt in write and simultaneously reading form file 1 and writing to file 2
with open("Origin.txt","r") as r, open("Dups.txt","w") as w:
    w.write(r.read())

#Printing result
r = open("Origin.txt")
print(f"1. The original text was: \n\n{r.read()}")

w = open("Dups.txt")
print(f"\n2. The Dublicate text is: \n\n{w.read()}")