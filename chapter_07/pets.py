"""_Removing all instances of specific values from a list_:
        0. Run a while loop until the value is no longer in our list.
"""

#Remove 'cat' from the pet list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)