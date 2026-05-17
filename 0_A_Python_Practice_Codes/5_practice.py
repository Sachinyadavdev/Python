# Challenge 2: The Grading System
# Task: Create a variable called score.

# If score is 90 or above, print "Grade: A".

# If score is 80 to 89, print "Grade: B".

# If score is 70 to 79, print "Grade: C".

# Anything below 70, print "Grade: F".

score = input("Enter Your Scrore: ")
score = int(score)

if (score > 89 ):
 print("You got the Grade A")

elif (score > 79 and score < 90):
 print("You got the Grade B")

elif (score > 69 and score < 80):
 print("You got the Grade C")

else:
 print ("You are fail")


# Task: Create two variables: username and password. Write an if statement that prints "Access Granted" only if the username is "admin" and the password is "12345". Otherwise, print "Access Denied".

username = "admin"
password = "12345"

input_username = input("Enter Your Username: ")
input_password = input("Enter Your Password: ")

if (input_username == username and input_password == password):
  print("Access Granted")

else:
  print("Access Denied")