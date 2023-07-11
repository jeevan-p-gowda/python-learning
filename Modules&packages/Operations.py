# Approach 1 - accessing other .py
import Calculator
import Animal

Calculator.add(1, 2)
Calculator.mul(3, 2)

Animal.bird()
Animal.lion()

# Approach 2 - accessing all from other .py
from Calculator import *

add(3, 2)
mul(4, 5)

# Approach 3 - accessing specific method
from Calculator import add

add(6, 7)

import Sample1
import Sample2

obj = Sample1.Sample1()
obj.meth1()

obj1 = Sample2.Sample2()
obj1.meth2()

from Sample1 import Sample1
from Sample2 import Sample2

ob = Sample1()
ob.meth1()

ob1 = Sample2()
ob1.meth2()
