"""_Passing an arbitrary number of arguments_:
        0. At times we won't know how many arguments a function needs to accept.
        1. Python allows a function to collect an arbitrary number of arguments from the calling statement.
"""

#Consider a function that build pizza without knowing the number of topppings.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'olives', 'extra cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
make_pizza('pepperoni')
make_pizza('mushroom', 'olive', 'extra cheese')

"""_Mixing positional and arbitrary arguments_:
        0. You can accept several different kinds of arguments.
        1. The parameter accepting the arbitrary argument must be placed last in the function definition.
        2. Python matches positional and keyword arguments first,
        3. Then collects any remaining arguments in the final parameter.
"""

#If our function needs to take in the size of the pizza ~ it must come before *toppings
def make_pizza(size, *toppings):
    """Summarize the pizza that we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'olives', 'extra cheese')