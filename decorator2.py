from decorator1 import main, larger

def decorator(func):
    def wrapper(text):
        print("Hello this is a decorator", end = " for ")
        func(text)
    return wrapper

@decorator
def call_main(text):
    main(text)

call_main("flowers")