x = 100
y = 10.1
z = "Python"
s = 'Welcome'
a = 'A'
b = "B"
c = True
d = False

# prints the data type
print(type(x))
print(type(y))
print(type(z))
print(type(s))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

h = i = j = 100
print(h, j, i)

k = 1
l = 2
print(k, l)

k, l = l, k
print(k, l)

m = 100
print(m)
m = "ABCD"
print(m)

# deleting variable
# del m
# print(m)

# Global and local variable
global_var = 10
xy = 30


def myFun():
    local_var = 20
    xy = 40
    print(xy)
    print(local_var)
    print(global_var)


myFun()


# change the global variable within the fun()
def myFun1():
    global global_var
    global_var = 99
    print(global_var)


myFun1()
print(global_var)  # it will print the modified value
