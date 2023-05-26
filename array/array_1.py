import array as arr

numbers = arr.array('i',[0,1,2,3,4,5,6,7,8,9])

print(numbers)
# access elements from array using slicing
print(numbers[2:5])

# extend original array with array given as argument
numbers.extend([23,34,45])
print(numbers)

# delete element form array using del method by passing index

del numbers[10]
print(numbers)

# remove an element by passing that element to remove method

numbers.remove(45)
print(numbers)

# append an item to array
numbers.append(165)
print(numbers)

# we can take out an element with index reference and assign to a variable using pop method
a = numbers.pop(11)
print(a)

# we can delete an array completely using del method

del numbers


try:
    print(numbers)
except NameError:
    print("variable named numbers already deleted.")
    
