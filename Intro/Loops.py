print('printing numbers between range')
print(list(range(10)))  # [0,1,2,3,4,5,6,7,8,9]
print(list(range(5, 10)))  # [5,6,7,8,9,10]
print(list(range(10, 1, -1)))  # [5,6,7,8,9,10]
print(list(range(-10, -5)))  # [-10,-9,-8,-7,-6]

print('print even numbers')
print(list(range(0, 10, 2)))
print(list(range(-10, 0, 2)))
print(list(range(10, 0, -2)))

print('print odd numbers')
print(list(range(1, 10, 2)))

print('while loop')
print('printing numbers in ascending order')
i = 1
while i <= 10:
    print(i)
    i = i + 1

print('printing numbers in descending order')
i = 10
while i >= 1:
    print(i)
    i = i - 1
print('Done!!')

for i in range(10):
    print(i)
print('Finished')

print('printing numbers using for loop')
for i in range(1, 10):
    print(i)

print('printing even numbers using for loop')
for i in range(0, 21, 2):
    print(i)

print('printing numbers in descending using for loop')
for i in range(10, 0, -1):
    print(i)

print('Jumping statements')
print('break')
for i in range(10):
    if i == 5:
        break
    print(i)

print('continue')
for i in range(10):
    if i == 5 or i == 3:
        continue
    print(i)
