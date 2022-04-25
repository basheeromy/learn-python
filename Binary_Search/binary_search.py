# this set of code is following binary serch algorithm
# for this type of algorithms, array should be sorted

from math import floor


a = [25,28,34,43,48,54,78,85,89,90,96,98]
n = len(a)
r = n-1
l = 0
data = int (input("give the number to find it's position : \n" ))
while l <= r :
    mid =int(floor (l+r)/2)
    if data == a[mid]:
        print (f"position of the given item is {(mid+1)}")
        break
    elif data < a[mid]:
        r = mid - 1
    else :
        l = mid + 1
else:
    print ("data not found")