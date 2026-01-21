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

def repeat(n):
    def decorator(func):
        def warpper(arg):
            for _ in range(n):
                func(arg)
        return warpper

    return decorator    

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
