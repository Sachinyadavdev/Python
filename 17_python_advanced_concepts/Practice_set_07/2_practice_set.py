import time

def timer(func):
    def wrapper(n):
        t1 = time.time()
        result = func(n)
        t2 = time.time()
        t3 = t2 - t1
        print(f"Time taken to execute {func.__name__} is {t3} seconds")
        return result
    return wrapper

@timer
def sum_m(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print("The sum is", sum_m(2000000))