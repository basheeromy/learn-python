import copy
# when we use = operator to make copy of an object, it only stores reference to 
# actual memory location (id of the object) to variable. 
# if we need an entire new copy instead of sharing same id, we can import and use copy module from python
# There are two types of copying in python, Shallow copy and deep copy
arr = [[1,2,3],[3,4,5]]
array = arr
print(f"id of arr : {id(arr)}")
print(f"id of arry : {id(array)}")

# in above given example, we can see that both arr and array have same id.

# Shallow copy
# A shallow copy creates a new object which stores the reference of the original elements.

# So, a shallow copy doesn't create a copy of nested objects, instead 
# it just copies the reference of nested objects. This means, a copy 
# process does not recurse or create copies of nested objects itself.

# shallow copy syntax

old_list = [[1,2,3],[2,12,3],['a','b','c']]
new_list = copy.copy(old_list)
print(f"id of old list : {id(old_list)}")
print(f"id of new_list : {id(new_list)}")

# here, we can see old_list and new_list have two different ids stored
old_list[1][1] = "added"
print(new_list)
print(old_list)

# as shallow copying copy nested objects' references, we can see the
# changes made in nested objects affects both lists


# to create completely different object including nested objects too,
# we can use deep copy function.

second_list = copy.deepcopy(old_list)
print(f"id of first nested object in old_list : {id(old_list[1])}")
print(f"id of first nested object in new_list : {id(new_list[1])}")
print(f"id of first nested object in second_list created with deep copy  : {id(second_list[1])}")