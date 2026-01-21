def decorator(func):
    def warpper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return warpper

@decorator
def say_hello():
    print("Hello!")

say_hello()