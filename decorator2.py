import time
from decorator1 import main, larger

def decorator(func):
    def wrapper(text):
        start = time.time()
        print("Hello this is a decorator", end = " for ")
        func(text)
        end = time.time()
        print(f"This function tookq {end - start} seconds")
    return wrapper

@decorator
def call_main(text):
    main(text)

call_main("flowers")