"""_Storing your function in modules_:
        0. An advantage of functions is the way they seperate block of codes from your main program.
        1. Your program will be easier to follow if you use descriptive names for your functions.
        2. You store your functions in a seperate file called modules and import it into your program.
        3. An import statement makes the code in a module available in your current running program file.
        4. Stiring functions in a seperate files allows you to focus on higher-level logic.
        5. Allows you to reuse functions in many different programs.
        6. Knowing how to import functions allows you to use libraries of functions other programmers have written.
        7. Ways to import a module:
"""

"""Import an entire module
    0. To start importing functions, we first create a module.
    1. A module is file ending in .py that contains the code you want to import into your program.
"""

#Make a module that contains the function make_pizza()
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
#Make a seperate file called making_pizza_10.py