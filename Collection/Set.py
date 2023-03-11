# Set is unordered and unindexed. It is enclosed in {}. It is mutable
mySet = {'apple', 'cherry', 'banana'}
print(mySet)

# read values through loop
print('--Read values through loop--')
for i in mySet:
    print(i)

print('--Check presence of item--')
if 'apple' in mySet:
    print('It is present')
else:
    print('It is not present')

# add items to the set
print('--add items to the set--')
mySet.add('melon')  # adds only single value
print(mySet)
mySet.update(['grapes', 'berry'])  # adds multiple values
print(mySet)

# find number of items in the set
print('--print no of items in the set--')
print(len(mySet))

# remove the item
print('--remove the item--')
mySet.remove('berry')  # should mention only existing value or else it will throw keyError
mySet.discard('xyz')  # can mention non-existing value, it will not throw any error
print(mySet)

# clear the set
# print('--clearing the set--')
# mySet.clear()
# print(mySet)

# deletes the set
# del mySet
# print(mySet)

# combine the set
print('--joins the set--')
mySet1 = {0, 2, 3}
# mySet2 = mySet.union(mySet1)
# print(mySet2)
mySet.update(mySet1)
print(mySet)

