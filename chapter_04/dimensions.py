"""_Tuples_: An immutable list. A list that can't be changed or modified. We use () instead of [].
        1. Tuples are simple data structures.
        2. Use them when you have to store a set of values that shouldn't be changed throughout the life of a program.
        NB: If you want to define a tuple with only one element, you need to include a trailing comma.
"""
#Create a tuple 
dimensions = (200, 50)
print(dimensions[0]) 
print(dimensions[1])

#Try change or reassign the first element on the list
dimensions[0] = 250 #You get a TypeError as you're not allowed to change elements in a tuple

#Create a tuple with only one element
my_t = (3, )
print(my_t)

#Looping through all values in a Tuple ~ Loops works the same just as in lists
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
    
#Writing over a Tuple
dimensions = (200, 50)
print("Oringial dimensions:")
for dimension in dimensions:
    print(dimension)
    
#Modifying a Tuple can be done by reassigning it to a new variable  
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
