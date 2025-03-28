def change_word():
    with open("Origin.txt", "r") as file:
        print("Choose a word from this text:\n")
        content = file.read()
        print(content)
    
    word = input("Enter the word you want to change: ")
    new_word = input(f"Enter what word you want to change '{word}' into: ")
    
    if word in content:
        updated_content = content.replace(word, new_word)
    else:
        updated_content = content.replace(word, word)

    with open("Origin.txt", "w") as file:
        file.write(updated_content)
    
    print("\nUpdated text:")
    print(updated_content)

change_word()