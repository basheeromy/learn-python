# radix sort in python 
def counting_sort(array,place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # store number of occurances in count array
    for i in range (0,size):
        index = array [i]//place
        count[index % 10] += 1
    
    # store cumulative count
    for i in range (1,10):
        count[i] += count[i - 1]

    # find the index of each element of original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        index = array[i]//place
        output[count[index % 10]-1] = array[i]
        count[index % 10] -= 1
        i -= 1
    # copy the store elements into original array
    for i in range (0,size):
        array[i] = output[i]


# main function to implement radix sort algorithm
def radixSort(array):
    # get maximum element 
    max_element = max(array)
    # apply counting sort
    place = 1
    while max_element//place > 0:
        counting_sort(array,place)
        place *= 10


# test code

data = [121,2,345,4235,564,23,1]
radixSort(data)
print (data)