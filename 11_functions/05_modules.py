# Two types of modules in Python:
# - Built in Modules
# - External Modules
# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
import math
import os
import mymodule

try:
    import requests
except ModuleNotFoundError:
    requests = None
    print("requests module is not installed. Falling back to urllib.request.")

print(math.sqrt(16))
mymodule.hello()

url = "https://www.google.com"
if requests:
    r = requests.get(url)
    print(r.text)
else:
    import urllib.request

    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))

# My Practices
print(math.sqrt(4))