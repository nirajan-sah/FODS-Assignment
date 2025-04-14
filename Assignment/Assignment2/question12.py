'''
program to find common words between two words
'''

#Function to do calculation
def word_intersection():

    #Prompt user for input and lower-case the input
    w1 = str(input("Enter first word: ")).lower()
    w2 = str(input("Enter second word: ")).lower()
    
    #use set to find intersetion between words
    common_word = set(w1).intersection(set(w2))

    print("The Common word are: ",common_word)

word_intersection()