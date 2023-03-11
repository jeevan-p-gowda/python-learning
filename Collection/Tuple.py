# Tuple is ordered and unchangeable. Tuple is immutable. It is enclosed with (). It is secure
myTupple = ('apple', 'banana', 'cherry', 'strawberry')
emptyTupple = ()

print(myTupple[0])
print(myTupple[1])
print(myTupple[1:4])
print(myTupple[-4:-1])

# change the items - can do by converting tuple into list
# adding and removing item is not possible
print('--converting tuple to list--')
myList = list(myTupple)
print(myList)
myList[0] = 'orange'
myTupple = tuple(myList)
print(myTupple)

# reading tuple items
for i in myTupple:
    print(i)

# find if value is present
print('--check value is present--')
if 'orange' in myTupple:
    print('yes present')
else:
    print('not present')

# find length of tuple
print('--length of the tupple--')
print(len(myTupple))

# copy tuple
myTupple1 = myTupple
print(myTupple1)

# deleting tuple
# del myTupple
# print(myTupple)

# joining tuple
tuple = myTupple + myTupple1
print(tuple)

# compare tuple
# can compare list too
print('--Compare tuples--')
if myTupple == myTupple1:
    print('equal')
else:
    print('not equal')
