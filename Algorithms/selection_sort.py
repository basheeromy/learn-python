# this code is following selection sort algorithm

a =  [7,4,10,8,3,1,89,990]
n = len (a)
# first loop to iterate over each set of comparison loop

for i in range (0,n-2):
    min = i
    # second loop iterates for comparison
    for j in range ((i+1),(n-1)):
        if a[j] < a[min]:
            min = j
    if min != i:
        temp = a[i]
        a[i] = a[min]
        a[min] = temp

print (a)