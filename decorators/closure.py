"""
    Closure is a function which remembers the 
    free variable from it's creation environment
"""

def outer_function(msg):
    def inner_funtion():
        print(msg)
    return inner_funtion


test = outer_function('this works')
test2 = outer_function('This also works')

test()
test2()

# we are printing the msg from the inner function. but, we passed 
# the msg to outer function, as a function has access to variables 
# from it's creation environment, inner function can access msg. 
# outer function returns the inner function as ready to execute. so 
# each time when we pass argument value to outer function and assign 
# the outer function to a variable, we are assigning closure to the 
# variable with the respective value.