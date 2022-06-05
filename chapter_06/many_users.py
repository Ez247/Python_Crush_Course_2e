"""_A dictionary in a dictionary_:
        0. You can nest a dictionary inside a dictionary.
        1. This can get a bit complicated at times.
"""

#Define a dictionary called users
users = {
    'aeistein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():                   #loop through the user dictionry
    print(f"\nUsername: {username}")                        #print the username
    full_name = f"{user_info['first']} {user_info['last']}" #access the inner dictionary for user info
    location = user_info['location']                        #access the inner dictionary for user location
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")