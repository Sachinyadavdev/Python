# Challenge 1: The Contact Book (Dictionary Basics)
# Task: Create a dictionary called user_profile that stores a person's information.

# Include keys for "name", "role", and "experience" (e.g., "Sachin", "Developer", 3).

# Add a new key-value pair for "location" and set it to "Chennai".

# Update the "experience" value to 4.

# Print the final dictionary.

user_profile = {"Name":"Sachin", "Experience": 3, "Role":"Developer"}

print("Initial Profile:", user_profile)

# CORRECT WAY TO ADD: Just use the new key inside brackets
user_profile["Location"] = "Chennai"

# Correct way to update
user_profile["Experience"] = 4

user_profile["Village"] = "Amarupur"

print("Updated Profile:", user_profile)

# Challenge 2: Word Frequency Counter (Looping over Data)
# Task: Write a script that takes a list of strings and counts how many times each item appears, storing the results in a dictionary.

# Input List: ["python", "javascript", "python", "java", "python", "javascript"]

# Expected Output: {'python': 3, 'javascript': 2, 'java': 1}

# Hint: Start with an empty dictionary {}. Loop through the list; if the word is already a key in your dictionary, increase its value by 1. If it's not, add it with a value of 1.

words = ["python","javascript", "java", "sachin", "sachin", "sachin", "sachin"]

frequency ={}

for word in words:
    if word in frequency:
        frequency[word] +=1

    else:
        frequency[word] = 1

print(frequency)

# Challenge 3: Nested Data Extraction
# Task: In real-world software development, data often arrives as nested structures (like JSON from an API). Given the following dictionary, write a single print statement that extracts and displays the second tool in the developer's tech stack.

developer_data = {
    "employee_id": 1024,
    "skills": {
        "primary": "Backend",
        "tools": ["Git", "Docker", "Firebase"]
    }
}

print(developer_data["skills"]["tools"][1])