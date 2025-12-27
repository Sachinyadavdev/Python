import requests

i=0
while i<20000:
    r = requests.get("https://pepsindia.com/")
    print(r.status_code)
    i+=1
    print(i)

