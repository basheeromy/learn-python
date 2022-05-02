# set of codes in insertion sort algorithm
# sort an array 
arr = [3,6,5,8,12,45,67,89,54,43]
for i in range (1,len(arr)):
    temp = arr[i]
    j= i-1

    while j >= 0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = temp

print (arr)
# time complexity of this algorithm is O(n^2)