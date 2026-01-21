# generic imports all the module

import random

print(random.randint(1,10))

# function import, imports single function

from random import randint , random

print(randint(10,20))
print(random())

#universal import, imports every function
from random import *



# python uses sys.modules for caching imported modules
# and uses sys.path for module importing
# Python runs the code inside the module once and creates a module object.


# import numpy as np       # gives module a shorter name
# from math import sqrt as sq