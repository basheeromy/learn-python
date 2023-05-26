"""
    A decorator is a design pattern in Python that 
    allows a user to add new functionality to an 
    existing object without modifying its structure
"""

def decorator_func(original_func):
    def wrapper_func():
        print("Wrapper executed this befor this {} function".format(original_func.__name__))
        original_func()
    return wrapper_func

@decorator_func
def display():
    print("This executed from original function")
    
display()
    