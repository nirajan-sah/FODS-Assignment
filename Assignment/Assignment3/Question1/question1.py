'''
Program to count number of lines, words and characters in a text file
'''

#opening origin.txt in read mode
f = open("Origin.txt", "r")

#function to read line
def num_line(f):
    length_line = 0
    #loop through whole line and add to length_line
    for line in f:
        length_line += 1

    print("The number of lines are:",length_line)
    
num_line(f)

#function to calculate number of elements
def num_char(f):
    #bringing cursor to 0 position
    f.seek(0)
    length_char = 0
    
    #Loop through lines
    for line in f:
        #loop through words
        for _ in line:
            length_char += 1
    print("The number of characters are:",length_char)

num_char(f)

#function to calculate words
def num_word(f):
    f.seek(0)
    f = f.read()
    #spliting all the words
    words = f.split()
    length = len(words)
    print("The number of words are:",length)

num_word(f)