print("This is starting point of program")

try:
    print(x)
except:
    print("Exception handled")

print("This is end of program")

# if we want except particular exception

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Exception occured and handled")

try:
    print("Hi")
except:
    print("Exception handled")
else:
    print("No exception handled")
finally:
    print("always execute")


# raise our own exceptions / user defined exceptions
def enterAge(num):
    if num < 0:
        raise ValueError("Only integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


enterAge(10)
try:
    enterAge(-1)
except:
    print("**Handled**")
