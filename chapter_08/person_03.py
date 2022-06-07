"""Returning a Dictionary:
        0. NB: A function can return any kind of values, eg lists and dictionaries.
"""
#Example
def build_person(first_name, last_name):
    """Return a dictionary of inforamtion about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

best_player = build_person('christiano', 'ronaldo')
print(best_player)

""""Extend this function to accept the following optional values:
        1. middle name
        2. age
        3. occupation
"""
def build_person2(first_name, last_name, middle_name=None, age=None, occupation=None):
    """Return a dictionary of inforamtion about person2"""
    person2 = {'first': first_name, 'last': last_name}
    if middle_name:
        person2['middle_name'] = middle_name
    if age:
        person2['age'] = age
    if occupation:
        person2['occupation'] = occupation
    return person2    

best_footballer = build_person2('christiano', 'ronaldo', age=37, occupation= 'soccer player', middle_name= 'dos santos')
print(best_footballer)