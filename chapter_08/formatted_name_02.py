"""_Return Values_:
        0. This are values that functions return after processing some data.
        1. They allow us to move much of our program's work into functions.
"""
"""Returning a Simple Value"""
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

footballer = get_formatted_name('christiano', 'ronaldo')
print(footballer)

"""Making an Argument optional:
        0. At time we want to make an argument optional so people using the function can
           choose to provide extra information only if they want to.
        1. We can use the default values set to an empty string to make an argument optional.
"""
#Include the option for user to include a middle name
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
        
footballer2 = get_formatted_name('leo', 'messi')
print(footballer2)
footballer3 = get_formatted_name('paul', 'pogba', 'labile')
print(footballer3)