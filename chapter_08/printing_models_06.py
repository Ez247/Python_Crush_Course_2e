"""_Modifying a list in a function_:
        0. When you pass a liat to a function, the function can modify the list.
        1. Any changes made to the list inside the function's body are permanent.
"""

"""For a 3D printing company:
        0. Create a list of designs that needs to be printed.
        1. Move the printed designs to a seperate kist.
"""
#Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
#Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
    
#Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    
"""A more carefully structured program:
        0. Define the first function that handles printing the designs.
        1. Definea second function that summarizes the print that have been made.
        2. EVERY FUNCTION SHOULD HAVEONE SPECIFIC JOB.
"""
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until nore are left.
    Move each design to completed_models afte printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}.")
        completed_models.append(current_design.title())
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe Following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['jaguar', 'bmw', 'honda', 'mercedes']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
    Preventing a function from modifying a list:
        0. At times you may want to prevent a function from modifying a list.
        1. To do this, pass the function a copy of the list like this:
            function_name(list_name[:]) ~ This makes a copy of the list to send through the function.
"""
#Make a copy of our unprinted_designs so we have a record of all the unprinted designs.
def print_models(unprinted_designs[:], completed_models):