def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks 
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, Marie=90, Priya=45)

def name_and_age(**kwargs):
    for item in kwargs.keys():
        print(f"{item} is {kwargs[item]} years old")

name_and_age(shubham=23, vikrant=34, jack=45, Marie=56, Priya=67, Mohan=78)