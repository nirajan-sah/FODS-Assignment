f = open("Origin.txt", "r")

def num_line(f):
    length_line = 0
    for _ in f:
        length_line += 1

    print(length_line)
    
num_line(f)

def num_char(f):
    f.seek(0)
    length_char = 0
    for line in f:
        for _ in line:
            length_char += 1
    print(length_char)

num_char(f)

def num_word(f):
    f.seek(0)
    f = f.read()
    words = f.split()
    length = len(words)
    print(length)

num_word(f)