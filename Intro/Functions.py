# Function without parameter and return type
def myFun():
    print('Welcome')


myFun()


# Function with parameter and without return type
def myFun1(name):
    print('Welcome', name)


myFun1('Jeevan')


# Function with parameter and return type
def myFun2(a, b):
    return a + b


print(myFun2(10, 20))  # positional arguments
print(myFun2(b=10, a=20))  # keyword arguments


# Function with no return
def myFun3():
    return


print(myFun3())


# can mention default values in argument itself
def myFun4(i, j=10):
    print(i, j)


myFun4(90)
myFun4(90, 70)  # can re-initialize the default value
myFun4(j=50, i=33)
myFun4(44, j=50)  # combination argument


def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a


print(largest(20, 10))
print(largest(10, 50))
