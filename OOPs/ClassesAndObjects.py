i, j = 1, 2  # global variables


class MyClass:
    a, b = 10, "hi"  # class variables

    def __init__(self, name):
        self.sample = name  # can create class variable inside method directly, no need to mention in class
        print(name)
        print("this is a constructor")

    # string type of constructor, only returns
    def __str__(self):
        return self.sample

    def myFun(self):  # self represents the class
        pass

    def display(self):
        print(self.sample)
        print(i, j)
        print('John')

    def printVariables(self, i, j):
        print(self.a, self.b)  # class variables accessed
        print(i, j)  # local variables accessed
        print(globals()['i'],
              globals()['j'])  # global variables accessed - use this when local variables have same name

    @staticmethod
    def staticMethod():
        print("This is a static method")


mc1 = MyClass('Jeevan')
print(mc1)  # prints the string constructor
mc1.myFun()
mc1.display()
mc1.printVariables(9, 8)
# static method can be accessed directly through class
MyClass.staticMethod()
