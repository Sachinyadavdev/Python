# text = "Python Programming"

# print(text[::3])
# print(len(text))
# print(text[5:-2])

# text2 =" i love python programming "

# print(text2.strip())
# print(text2.title())

# print(text2.find("o"))
# print(text2.replace("o", "1"))
# print(text2.count("o"))

# is_alpha = "123abc"

# print(is_alpha.isalnum())  # True

message = (input("Enter your text: "))

print(message)

print("The a vowel is :",message.count("a"))
print("The e vowel is :",message.count("e"))
print("The i vowel is :",message.count("i"))
print("The o vowel is :",message.count("o"))
print("The u vowel is :",message.count("u"))

a= message.count("a")
e= message.count("e")
i= message.count("i")
o= message.count("o")
u= message.count("u")

sum = a + e + i + o + u
print("Total number of vowels in the text is :", sum)


# Checking the Palindrome

text2 = input("Enter the text to check palindrome: ")

if text2 == text2[::-1]:
    print("The text is Palindrome")
else:
    print("The text is not Palindrome")

    

