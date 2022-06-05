"""_A dictionary of similar objects_: 
            1. You can use a dictionary to store one kind of information about many objects.
"""

#Poll people on their favorite programming language
favorite_languages = {
    'dave': 'c',
    'erin': 'python',
    'alice': 'ruby',
    'john': 'java',
    }

language = favorite_languages['erin'].title()
print(f"Erin's favorite language is {language}.")