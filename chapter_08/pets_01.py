"""_Passing Arguments_:
        0. Function definitions can have multiple parameter.
        1. A function call may need multiple arguments. This can be done in a number of ways:     
            a. Positional arguments.
            b. Keyword arguments.
            c. Default values.     
"""

"""a. Positional arguments:
        i. This need to be in the same order the parameters were written: Key arguments:
            a. where each argument consists of a variable name and , and
            b. lists and dictionaries of values.
"""

"""Positional Arguments"""
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')

"""Multiple function calls:
        a. You can call a function as many times as needed.
"""
describe_pet('cat', 'henny')
describe_pet('dog', 'bruce')

"""Order matters in positional arguments:
        a. You can get unexpected results if you mix uo your order of arguments.
"""
describe_pet('bruce', 'dog')

print("\n______________________________________________")


"""b. Keyword arguments:
        i. A name-value pair that you pass to a function.
       ii. You directly associate the name and value within the argument.
      iii. This prevents mix ups.  
"""
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

print("\n______________________________________________")

"""c. Default Values:
        i. You can define a default value for each parameter. 
       ii. This can simplify your functions calls and clarify ways in which functions are typically used.
"""
#If all our animal types are dog
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='wallace')
#This is a simplified way to call the function describe_pet
describe_pet('wallace')