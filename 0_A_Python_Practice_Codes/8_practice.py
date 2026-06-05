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
