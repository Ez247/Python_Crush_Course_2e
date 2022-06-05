"""_Testing Multiple Conditions_: Sometimes we want to check all the condition.
        1. In this case, we use a series of if statements with no elif or else block.
        2. Makes sense when more than one of our condition could be True, and
        3. We want to act on every condition that is True.
"""

#Check if someone requested a two-topping pizza

requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'olives' in requested_toppings:
    print('Adding olives.')
    
print("\nFinished making your pizza!")