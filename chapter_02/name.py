"""_strings_: A series of characters.
    NB: Anything inside quotes(double or single) is considered a string. 
"""
#Example
"This is an example of a string."
"This is also considered a string."

#Changing Case in a String with Methods.
"""_Method_: An action that Python can perform on a piece of data.
    One of the simplest task you can do with strings is change the case of a string.
    Things to note about methods:
        1. Every method is followed with a parenthesis(), e.g title(), lower() etc
        2. The lower() method is useful for storing data. 
"""

#Using methods
name = 'kevin smith'
print(name.title()) #title() capitalizes the first letters of the name
print(name.lower()) #lower() prints the name to lower case or small letters
print(name.upper()) #upper() capitalizes all the letter in the variable name.