# List is ordered and changeable. List is mutable. It is enclosed with []

myList1 = [10, 20, 30, 40]
myList2 = ['apple', 'banana', 'cherry', 'strawberry']
myList3 = ['monkey', 20, 'donkey', 40]
myList4 = list()

print(myList2)
print(myList2[0])
print(myList2[-1])
print(myList2[1:3])
print(myList2[-3:-1])

# Change item value
myList2[0] = 'orange'
print(myList2)

# print using for loop
for i in myList2:
    print(i)

# find if value is present
if 'orange' in myList2:
    print('yes present')
else:
    print('not present')

# find length of list
print(len(myList2))

# add item to the list
myList2.append('melon')
print(myList2)
myList2.insert(1, 'Kiwi')
print(myList2)

# remove item from the list
myList2.pop(0)
print(myList2)
del myList2[2]
print(myList2)
# myList2.clear()
# print(myList2)

# copy list
myList5 = list(myList2)
print(myList2, myList5)
myList6 = myList2.copy()
print(myList6)

# combine list
myList7 = myList2 + myList1
print(myList7)

# using loop statement
for i in myList2:
    myList6.append(i)
print(myList6)

myList2.extend(myList1)
print(myList2)

# sorting - can be done in two ways
li = [2, 9, 1, 5, 4, 7, 6]
li2 = [-6, -5, -4, 1, 2, 3]
print('Original list {}'.format(li))
# Approach - 1
# li.sort()
# li.sort(reverse=True)
# Approach - 2 - It is preferred because can sort any iterables like dict, list, tuple
s_li = sorted(li)
s_r_li = sorted(li, reverse=True)
print('Sorted list {}'.format(s_li))
print('Reversed list {}'.format(s_r_li))
# using key=abs neglects whatever the sign may be assigned
s_r_li2 = sorted(li2, key=abs)
print('Sorted list irrespective of sign', s_r_li2)
