"""
    There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
"""
def getTotalX(a, b):
    elCons = []
    facto = []
    for i in b:
        for j in range(2,i+1):
            if i % j == 0:
                is_f = True
                for k in b:
                    if k % j != 0:
                        is_f = False
                if j not in facto and is_f == True:
                    facto.append(j)
    print(facto)
    for i in facto:
        is_con = True
        for j in a:
            if i % j != 0:
                is_con = False
        if is_con == True:
            if i not in (elCons):
                elCons.append(i)
    print(elCons)
    return len(elCons)

a = [2,4]
b = [16,32,96]
print(getTotalX(a,b))

# print(32 % 16)