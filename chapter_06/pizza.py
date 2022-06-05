"""_A list in a dictionary_:
        0. It's sometimes useful to put a list inside a dictionary.
"""

#Store information about a pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese', 'onions']
}

#Order summary
print(f"You order a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    
#A detailed example
favorite_languages = {
    'dave': ['python', 'ruby'],
    'alice': ['c'],
    'jen': ['ruby', 'go'],
    'paul': ['python', 'java'],
    }

for name, languages in favorite_languages.items():         #loop through the dictionary
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")