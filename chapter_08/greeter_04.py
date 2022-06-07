"""Using a Function with a while Loop:
        0. You can use functions with any Python data structure. Lists, Dictionaries and so on.
"""
#First attempt at greeting people using their first and last name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me you name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("Fitst name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    
    