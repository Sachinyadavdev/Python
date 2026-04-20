
def logger(func):
    def wrapper():
        print(f"Executing {func.__name__} function")
        func()
        print(f"Finished executing {func.__name__} function")
    return wrapper


@logger
def say_hello():
    print("Hello, World!")

say_hello()