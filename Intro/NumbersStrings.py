# find max and min number - using max/min function
print('Finding max number')
print(max(60, 80, 100))

print('Finding min number')
print(min(60, 80, 50))

# Strings
# Creating string and empty string
s1 = str('Welcome')
s2 = ''
s3 = str()

# Mutable - can change the of the variable, Immutable - we cannot change
print(id(s1))
print(id(s3))

# printing multiple times using *
print(s1 * 3)

# slicing[] (like substring)
print(s1[1:3])
print(s1[:6])
print(s1[0:])
print(s1[0:-2])  # -2 removes last 2 characters

# ord() - prints the ascii value, char() - prints the char of ascii value
print(ord('A'))
print(chr(65))

# find max and min char - using max/min function
print('Find max char')
print(max('abc'))

print('Find min char')
print(min('abc'))

# find length of string
print('Find length of string')
print(len('Welcome'))

# find the substring in given string - like boolean
print('--booleans--')
exmp = 'Sunrise'
print('rise' in exmp)
print('rise' not in exmp)
print('WELCOME'.isupper())
print('welcome'.islower())
print('1234'.isdigit())  # checks it contains any digit in string
print('1234'.isalnum())
print('welcome'.isalpha())
print('welcome'.isidentifier())  # checks it contains any keyword of python
print(' '.isspace())

# Searching for sub strings
print('--Searching sub strings--')
exmp1 = 'Sun rises in the east'
print(exmp1.startswith('Sun'))
print(exmp1.endswith('east'))
print(exmp1.find('rises'))  # gets the index num
print(exmp1.count('s'))  # gets the occurrence of character

# Converting strings
print('-Converting strings-')
exmp3 = 'string in PYTHON'
print(exmp3.capitalize())
print(exmp3.title())
print(exmp3.upper())
print(exmp3.lower())
print(exmp3.swapcase())
print(exmp3.replace('in', 'on'))

# Reverse a string
exmp4 = 'PyCharm'
rev_str = ' '
for i in exmp4:
    rev_str = i + rev_str
print('Actual String: %s, Reversed String: %s' % (exmp4, rev_str))

revStr = exmp4[::-1]
print(revStr)
