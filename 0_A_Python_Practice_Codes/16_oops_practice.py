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