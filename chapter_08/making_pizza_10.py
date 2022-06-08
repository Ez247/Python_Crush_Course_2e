"""Import the module we made in pizza_09.py"""
#Open the file pizza_09 and copy all functions from it into this program
import pizza_09

pizza_09.make_pizza(16, 'pepperoni')
pizza_09.make_pizza(12, 'mushroom', 'olives', 'extra cheese')

"""Importing specific functions:
        0. You can also import a specific funtion from a module.
         - from module_name import function_name 
"""

#Import the function make_pizza from from the module pizza_09
from pizza_09 import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'olives', 'extra cheese')

"""Using as to give a function an alias:
        0. You can provide an alias for a module name. 
         - import module_name as mn
"""
#Give pizza_09 the alias p
import pizza_09 as p 

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'olives', 'extra cheese')

"""Importing all functions in a module
        0. (*) imports every function in a module.
"""
from pizza_09 import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'olives', 'extra cheese')
