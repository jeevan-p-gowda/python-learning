# Dunder/magic are the functions which can be overridden and can be manipulated as per requirement.
class Employee:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal

    def __repr__(self):
        return 'Overriden object address using __repr__ {} {}'.format(self.name, self.age)

    def __str__(self):
        return 'default overidden method is __str__ {} {}'.format(self.name, self.age)

    def __add__(self, other):
        return self.sal + other.sal

    def __len__(self):
        return len(self.name)


employee1 = Employee('Corey', 45, 50000)
employee2 = Employee('Jeevan', 27, 30000)
print(employee1)
print(repr(employee1))
print(employee1+employee2)
print(len(employee1))
