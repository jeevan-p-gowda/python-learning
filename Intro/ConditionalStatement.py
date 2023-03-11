# Conditional statements - if, if..else, elif

print('--Print a person eligible to vote or not--')
age = 15
# age = int(input('Enter age: '))
if age >= 18:
    print('Eligible to vote')  # indentation is important here
else:
    print('Not Eligible to vote')  # indentation is important here

print('--Directly mentioning True/False--')
if True:
    print('True condition')
else:
    print('False condition')

print('--Directly mentioning True/False value--')
if 0:
    print('True condition')
else:
    print('False condition')

print('--Find Even/Odd number--')
num = 17
if num % 2 == 0:
    print('Its a Even number')
else:
    print('Its a Odd number')

print('--Find Even/Odd number in a single line using Ternary Operator--')
num = 10
print('Its a Even number') if num % 2 == 0 else print('Its a Odd number')

a = 5
{print('hello'), print('python')} if a >= 10 else {print('hi'), print('java')}

print('--elif--')
weekNo = 8
if weekNo == 1:
    print('Sunday')
elif weekNo == 2:
    print('Monday')
elif weekNo == 3:
    print('Tuesday')
elif weekNo == 4:
    print('Wednesday')
elif weekNo == 5:
    print('Thursday')
elif weekNo == 6:
    print('Friday')
elif weekNo == 7:
    print('Saturday')
else:
    print('Invalid week number')
