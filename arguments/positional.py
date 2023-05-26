"""
    During a function call, values passed through arguments
    should be in the order of parameters in the function 
    definition. This is called positional arguments.
"""

def position(a,b,c):
    return(f"a = {a},b = {b},c = {c}")
    
print(position(12,13,14))