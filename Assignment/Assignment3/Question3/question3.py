'''
program to find the replace a specific word by user
'''

#function to change_word
def change_word():

    #opening the file as read
    with open("Origin.txt", "r") as file:
        print("Choose a word from this text:\n")
        content = file.read()
        #printing the file so that user can choose certain word
        print(content)
    
    #prompting user what word they want to change to which word
    word = input("Enter the word you want to change: ")
    new_word = input(f"Enter what word you want to change '{word}' into: ")
    
    #if the word is found in content then it is replaced else all are same
    if word in content:
        updated_content = content.replace(word, new_word)
    else:
        updated_content = content.replace(word, word)

    #writing updated file to origin.txt
    with open("Origin.txt", "w") as file:
        file.write(updated_content)
    
    print("\nUpdated text:")
    print(updated_content)

change_word()