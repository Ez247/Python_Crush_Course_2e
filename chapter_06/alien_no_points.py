"""_Using get() to access values_: 
        0. Using keys to retrieve values from a dictionary might cause potential problems:
            a. If a key you want to retrieve doesn't exist, you'll get an error.
        1. You can use the get() method to set a default value that will be returned if 
           requested key doesn't exist.
        2. The get() method requires a key as a first argument.
        3. As a second optional argument, you can pass the value to be returned if the key doesn't exist.
"""

#Example
alien_0 = {'color': 'green', 'speed': 'medium'}
print(alien_0['points'])  #This results in a KeyError, points is not in our dictionary

point_value =  alien_0.get('points', 'No point value assigned.')
print(point_value)