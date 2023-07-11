# dictionary is unordered, changeable(mutable) and unindexed.
# It is enclosed with {} and has keys and values (like java hashmap)
myDic = {101: {1: "x"}, 102: 'y', 103: 'z'}
myDic1 = {101: {1: "x"}, 102: 'y', 103: 's'}
if myDic == myDic1:
    print("true")
else:
    print("false")

print(myDic)
print('fetching value')
print(myDic[101])
print(myDic.get(101))

# change value
print('--change value--')
myDic[101][1] = 's'
print(myDic)

for i in myDic:
    print(i)  # prints only keys
    print(myDic[i])  # prints values

print('--print only values--')
for i in myDic.values():
    print(i)

print('--print keys and values--')
for x, y in myDic.items():
    print(x, y)

# check key is in dictionary or not
print("--Check key/value presence--")
if 101 in myDic:
    print('Present')
else:
    print('Not present')

# find no of items in dictionary
print('--Length of items in dictionary--')
print(len(myDic))

# adding the item to dictionary
print('--adding item--')
myDic[104] = 'e'
print(myDic)

# remove the item
print('--remove the item--')
myDic.pop(101)
del myDic[102]
print(myDic)

# delete the dic
# print('--delete the dict--')
# del myDic

# clear the dict
# myDic.clear()
# print(myDic)

# copy the dict
print('--copy the dict--')
# myDic1 = myDic
myDic1 = myDic.copy()  # same result
print(myDic1)

myDic.update({'name': 'jeevan'})
print(myDic)
