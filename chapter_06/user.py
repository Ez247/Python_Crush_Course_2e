"""_Looping through all key-value pairs_:
"""

#Store user information on a website
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#To see every information about user_0
for key, value in user_0.items():   #loop through each key-value pair in the dictionary
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    
#Another example of looping through a dictionary
favorite_languages = {
    'dave': 'c',
    'erin': 'python',
    'alice': 'ruby',
    'john': 'java',
    }

for name, language in favorite_languages.items():    #Loop through each key-value pair in the dictionary
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
#Looping through all the keys in a dictionary 
#The key() method ~ useful when we don't have to work with all of the values in a dictionary.

favorite_languages = {
    'dave': 'c',
    'erin': 'python',
    'alice': 'ruby',
    'john': 'java',
    }

#Let's print the names of everyone who took the poll
for name in favorite_languages.keys():
    print(name.title())
    
#This also works. It's the default way to loop through a dictionary
for name in favorite_languages:
    print(name.title())
    
#Let's print a message to our friends about their favorite language.
friends = ['erin', 'john']  #Create a list of friends we want to print message to.
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:     #Check if the name is in our friends list
        language = favorite_languages[name].title() #determine person's favorite language
        print(f"\t{name.title()}, I see you love {language}!")
        
#Using keys() method to find out if a particular person was polled, eg 'phil
if 'phil' not in favorite_languages.keys():
    print('Phil, please take our poll.')
    
"""_Keys() Method_:
        0. Keys() method isn't just for looping.
        1. It also returns a list of all the keys in a dictionary.
"""

"""_Loopin through a dictionary's keys in a particular order_:
        0. Starting in Python 3.7, looping through a dictionary returns the items in the 
           same order they were inserted.
        1. At times we may want to loop through a dictionary in a different order.
        2. One way to do this ~ sort the keys as they're returned in the for loop.
        3. You can use the sorted() function to get a copy of the keys in order
"""

#Example
favorite_languages = {
    'dave': 'c',
    'erin': 'python',
    'alice': 'ruby',
    'john': 'java',
    'klay': 'python'
    }

for name in sorted(favorite_languages.keys()):  #List all the keys in the dict & sort the list before looping
    print(f"{name.title()}, thank you for taking the poll.")
    
"""_Looping through all values in a dictionary_:
        0. Use values() method is only interested in the values in a dictionary.
"""

#List all languages chosen in our peogramming language poll
print("The following languages have been mentioned:")
for language in favorite_languages.values():  #pull all values from the dict without check for repeats.
    print(language.title())
    
#To list only unique languages in our poll ~ use set()
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):  #Only identify unique items in our dictionary
    print(language.title())
    
"""_Note on sets_:
        0. You can build a set directly using braces & separating the elements with commas:
            languages = {'c', 'python', 'java', 'ruby', 'python'}
        1. Difference between sets and dictionaries & lists:
            a. Sets have no key-value pairs.
            b. Sets don't retain items in any specific order.
"""