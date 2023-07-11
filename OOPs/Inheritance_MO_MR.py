# print('--Single level inheritance--')


# class Sample1:
#     x, y = 10, "Jeevan"
#
#     def m1(self):
#         print("this is m1 method from class Sample1")
#
#
# class B(Sample1):
#     def m2(self):
#         print(self.x, self.y)
#         print("this is m2 method from class b")
#
#
# obj = B()
# obj.m1()
# obj.m2()


# print('--Multilevel level inheritance--')
#
#
# class Sample1:
#     x, y = 10, "Jeevan"
#
#     def m1(self):
#         print("this is m1 method from class Sample1")
#
#
# class B(Sample1):
#     i, j = 1, 2
#
#     def m2(self):
#         print(self.x, self.y)
#         print("this is m2 method from class B")
#
#
# class C(B):
#     def m3(self):
#         print(self.x, self.y)
#         print(self.i, self.j)
#         print("this is m3 method from class C")
#
#
# obj = C()
# obj.m1()
# obj.m2()
# obj.m3()

# print('--Hierarchical level inheritance--')
# class Sample1:
#     x, y = 10, "Jeevan"
#
#     def m1(self):
#         print("this is m1 method from class Sample1")
#
#
# class B(Sample1):
#     i, j = 1, 2
#
#     def m2(self):
#         print(self.x, self.y)
#         print("this is m2 method from class B")
#
#
# class C(Sample1):
#     def m3(self):
#         print(self.x, self.y)
#         print("this is m3 method from class C")
#
#
# obj = C()
# obj.m1()
# obj.m3()
#
# obj2 = B()
# obj2.m1()
# obj2.m2()
#
# print("--Multiple inheritance--")
#
#
# class Sample1:
#     x, y = 10, "Jeevan"
#
#     def m1(self):
#         print("this is m1 method from class Sample1")
#
#
# class B:
#     i, j = 1, 2
#
#     def m2(self):
#         # print(self.x, self.y)
#         print("this is m2 method from class B")
#

# class C(Sample1, B):
#     def m3(self):
#         print(self.x, self.y)
#         print(self.i, self.j)
#         print("this is m3 method from class C")
#
#
# obj = C()
# obj.m1()
# obj.m2()
# obj.m3()

# print("--Method Overiding--")
#
#
# class Sample:
#     name = "John"
#
#     def meth(self):
#         print(self.name)
#         print("Test Method")
#
#
# class OverRidingClass(Sample):
#     name = "David"
#
#     def meth(self):
#         print(self.name)
#         print("Overridden")
#         super().meth()
#         print(super().name)
#
#
# s = OverRidingClass()
# s.meth()

print("--Method Overloading--")


class Human:
    def sayHello(self, name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")


h = Human()
h.sayHello("Scott")
h.sayHello()

print("--Method Overloading 2 --")


class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


calObj = Calculation()
calObj.add()
calObj.add(10, 20)
calObj.add(10, 30, 40)
