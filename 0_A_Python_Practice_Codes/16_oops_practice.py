import requests

def check_site_status(link):

    try:
        r = requests.get(link)
        r.status_code
        if r.status_code == 200:
            print("Website is Working and it is not offline")

        else:
            print("Website is not working fine, Kindly asked the Developer to fix it!")

    except Exception as e:
        print("An error occurred:", e)

link = input("Enter the website link to check its status: ")
check_site_status(link)


# Challenge 2 :

# Challenge 2: Fetching Live Data (JSON)
# Task: When web servers talk to Python, they send data back in a format called JSON (which looks exactly like a Python Dictionary!). Let's fetch a live random joke from a free, open API.

# Send a GET request to this live URL: https://official-joke-api.appspot.com/random_joke

# Convert the response into a Python dictionary using the .json() method:

# Python
# data = response.json()
# Print the raw dictionary to see how it looks.

joke_r = requests.get("https://official-joke-api.appspot.com/random_joke")

data = joke_r.json()

print(joke_r)
print(data)

print(f"Setup : {data['setup']}")
print(f"Punchline : {data['punchline']}")

