# Challenge 1: The Note Taker (Writing)
# Task: Write a program that takes a string of text from a user (like a daily diary entry or a reminder) and saves it into a file named notes.txt.

# Hint: Use open("notes.txt", "w") — the "w" stands for write mode (warning: this overwrites the file if it already exists).

user_text = input("Enter the Note you want to take: ")

note = open("note.txt","w")

note.write(user_text)