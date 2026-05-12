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

