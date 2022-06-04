"""_Whitespace_: Anything that is nonprinting, spaces, tabs, and end-of-line symbols.
        1. Whitespace can be used to organize output so its' easier for user to read.
"""

#Using tab in your code. Add \t to the code
print('Python 3.9')
print('\tPython 3.9')

#Adding a newline in a string, use \n.
print("Languages:\nPython\nC\nJavaScript")

#You can also combine tabs abd newline in a string, "\n\t"
print("Languages:\n\tPython\n\tC\n\tJavaScript")


"""_Stripping Whitespace_strip(): Why it's important to think about whitespace:
        1. Checking people's username when they log in to a website.
        2. Compare if two strings are the same
        3. rstrip()  ~ removes whitespace to the right of a string.
        4. lstrip() ~ removes whitespace to the left of a string.
"""
#Using  strip()
favourite_language = ' Python '
favourite_language = favourite_language.strip()
print(favourite_language)