import sys

sys.path.append("C:/Users/JeevanP/Desktop/PythonLearning/Modules&packages/Package1")
sys.path.append("C:/Users/JeevanP/Desktop/PythonLearning/Modules&packages/Package1/SubPackage1")

import Module1
import Module2

Module1.display_info()
Module2.show()

from Module1 import *

display()
