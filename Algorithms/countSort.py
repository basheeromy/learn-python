def countingSort(array):
    size = len (array)
    output = [0] * size
    count = [0] * 10

    # store number of occurance of each element in count array
    for i in range (0,size):
        count[array[i]] += 1
    
    # store cumulative count
    for i in range (1,10):
        count[i] += count[i - 1]
    # find the index of each element of original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]]-1] = array[i]
        count [array[i]] -= 1
        i -= 1

    # copy the store elements into original array 
    for i in range (size-1):
        array [i] = output [i]


# test sorting algorithm 

data = [2,4,1,5,7,6,4,8,3,3,9]
countingSort(data)
print (data)