"""_Dictionaries_: Can store an almost limitless amount of information.
        0. A collection of key-value pairs.
        1. Allow us to connect pieces of related information.
        2. Allow us to access and modify information inside a dictionary.
        3. Loop through data inside a dictionary.
        4. Nest dictionaries inside lists, lists inside dictionaries, dictionaries inside dictionaries.
"""
"""_Working with Dictionaries{}_: 
        0. A collection of key-value pairs.
        1. Each key is connected to a value. NB: A key's value can be a number, string, a list or a dictionary.
        2. You can use a key to access the value associated with that key.
"""
#A simple dictionary
alien_0 = {'color': 'green', 'points': 5} #Store alien 0 color and points

#Accessing values in a dictionary
print(alien_0['color'])  #Access the value of the key color
print(alien_0['points']) #Accsss the value of the key points

#Assigning dictionary values to a variable
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Adding new key-value pairs to our dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0    #Add a new key-value pair, key 'x_position' & value 0
alien_0['y_position'] = 25   #Add a new key-value pair, key 'y_position' & value 25
print(alien_0)

#Starting with an empty dictionary
alien_0 = {}                #Start with an empty dictionary

alien_0['color'] = 'green'  #Add key-value pair, key 'color' & value 'green'
alien_0['points'] = 5       #Add key-value pair, key 'points' & value 5

print(alien_0)

#Modifying values in a dictionary ~ give the name of the dictionary & the new associated values
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'     #Change the value associated with the key 'color' to 'yellow'
print(f"The alien is now {alien_0['color']}.")

#Further examples of modifying dictionaries
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment = 3
    
#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")   

#Removing key-value pairs ~ use the del statement
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#Let's remove the key 'points' from alien_0 disctionary
del alien_0['points']   #Delete the key points from the dictionary
print(alien_0)

