"""_Passing a List_: 
        0. Often you will find it useful to pass a list to a function.
        1. When you do so the function gets direct access to the contents of the list.
"""

#Greet users in a list individually.
#Define greet_users function so it expects a list of names
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

#Define our list of users and pass it through our function        
usernames = ['hannah', 'rose', 'montana', 'jay']
greet_users(usernames)