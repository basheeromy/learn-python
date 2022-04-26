# here we are going to be familiar with bubble sort algorithm

a = [56,78,86,23,757,82,95,9,8,4]
b = len (a)
for i in range (b):
    swap = False
    for j in range (0,(b-i-1),):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]= temp
            swap = True
    if not swap:
        break
print (a)