import requests

r = requests.get('https://en.wikipedia.org/wiki/Sachin_Tendulkar')

s = requests.get('https://en.wikipedia.org/wiki/Sachin_Tendulkar')

with open("Sachin.txt", "w") as f:
    f.write(r.text)


with open("Sachin2.txt", "w") as f:
    f.write(s.text)

with open("Sachin2.txt", "r") as f:
    print(f.read())