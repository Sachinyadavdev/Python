# Challenge 1: The Note Taker (Writing)
# Task: Write a program that takes a string of text from a user (like a daily diary entry or a reminder) and saves it into a file named notes.txt.

# Hint: Use open("notes.txt", "w") — the "w" stands for write mode (warning: this overwrites the file if it already exists).

user_text = input("Enter the Note you want to take: ")

# note = open("note.txt","w")

# note.write(user_text)

# note.close()

# with open("note.txt","w") as note:
#     note.write(user_text)

print("Note has been save successfully!")


# Challenge 2: The Log Appender (Appending)
# Task: Imagine you are creating a system log. Write a script that adds a new line of text to your existing notes.txt file without deleting what was already there.

# Hint: Use "a" mode, which stands for append. It adds new data to the very end of the file. Don't forget to include a newline character (\n) so each entry goes on a fresh line!

with open("note.txt","a") as note:

    note.write(user_text + "\n")

# Challenge 3: The Memory Reader (Reading)
# Task: Write a script that opens your notes.txt file, reads all the content inside it, and prints it out to the console.

# Hint: Use "r" mode, which stands for read. You can use the .read() method on your file object to extract the text.

# How do these look? File handling is a huge milestone—once you master this, you can build programs that actually remember user data! Give it a shot.

with open("note.txt","r") as note:
    print(note.read())

