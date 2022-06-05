"""_Using if statements with Lists_: You can watch for special values that need to be treated differently.
"""

#Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your Pizza!")

#What if we ran out of green peppers?
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#Checking that a list is not empty.
requested_toppings = []

if requested_toppings:      #Check for requested toppings
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'onions', 'pineapple', 'extra cheese', 'steak']

requested_toppings = ['mushrooms', 'french fires', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")