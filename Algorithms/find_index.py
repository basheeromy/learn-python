# this program is written in linear search algorithm
Marks = [45,23,65,78,23,98,99,89,67,47]
mark = int(input('enter the mark to find its position in list\n'))
for i in range (len(Marks)):
    if Marks [i-1] == mark:
        print (f'position of the given number in list is {i}')
        break
else:
    print ('item not found')