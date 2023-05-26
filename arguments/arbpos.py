"""
    For arbitrary positional argument, an asterisk (*) is
    placed before a parameter in function definition which
    can hold non-keyword variable-length arguments. These 
    arguments will be wrapped up in a tuple. Before the 
    variable number of arguments, zero or more normal 
    arguments may occur.
"""

def arbpos(*a):
    return(a)

print(arbpos(1,2,3,4,5,6))