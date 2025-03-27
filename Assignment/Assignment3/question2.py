def change_word(word, New_word):
    file = open("Origin.txt", "r")
    content = file.read()

    if word in content:
        updated_content = content.replace(word, New_word)

    else:
        updated_content = content

    file_new = open("Temp.txt","w")
    file_new.write(updated_content)

    file_new.close()
    
    
change_word("name", "nam")