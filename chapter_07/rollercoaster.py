"""_Using int() to accept numerical inputs:
    0. Python inteprets everything the user enters as a string.
"""

#Example
height =  input("How tall are you, in inches? ")
height = int(height)

if height >= 48:     #Check if user is tall enough
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")