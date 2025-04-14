'''
Program to get word count of each word
It is done by using python library collection 
'''
from collections import Counter

def count_word_occurrences(file_path):
    try:
        # Open the file and read its content
        with open(file_path, 'r') as file:
            text = file.read()
        
        # Split the text into words (case insensitive)
        words = text.lower().split()

        # Count occurrences of each word
        word_counts = Counter(words)

        # Display word counts
        for word, count in word_counts.items():
            print(f"{word}: {count}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the file path
file_path = "Origin.txt"  # Replace with your file's path
count_word_occurrences(file_path)