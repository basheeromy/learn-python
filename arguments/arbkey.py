"""
    For arbitrary keyword argument, a double asterisk (**)
    is placed before a parameter in a function which can 
    hold keyword variable-length arguments.
"""

def arbkeys(**a):
    print(a)
        

arbkeys(cats = 4, rabits = 5, working = "Excellent")