# here we are going to be familiar with bubble sort algorithm

a = [1,2,3,4,5,9,7,8]
b = len (a)
for i in range (b):
    swap = False
    for j in range (0,(b-i-1),):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]= temp
            swap = True
            print ('i')
    if not swap:
        break
print (a)