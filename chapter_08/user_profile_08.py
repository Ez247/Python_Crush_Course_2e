"""_Using arbitrary keywird arguments_:
        0. At times you want to aacept an arbitrary number of arguments.
        1. In this case you write a functions that will accept as many key-value pairs.
"""

#Build a user profile function
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first 
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('kevin', 'smith',
                             location='atlanta',
                             field='comedy')
print(user_profile)