# Default arguments
"""
    *   Default arguments are values that are provided 
        while defining functions.
        
    *   Default arguments become optional during the function calls.
"""

def default(a=10,b=12):
    return a+b

# call the function without any arguments, then 
# function will use default arguments
print(default())

# If we provide a value to the default arguments during function calls, it overrides the default value.

print(default(5,6))

# Default arguments should follow non-default arguments.

def dfunction(a,b=10,c=56):
    return (a+b+c)

print(dfunction(29))