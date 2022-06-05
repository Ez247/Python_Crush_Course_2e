"""_Nesting_:
        0. At times you may want to store multiple dictionaries in a list, or a list of items as a value.
        1. You can nest dictionaries inside a list, a list of items inside a dictionary, dict inside a dict.
"""

#A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'red', 'points': 25}

aliens = [alien_0, alien_1, alien_2]    #Store our alien dictionaries in a list named aliens.

for alien in aliens:
    print(alien)
    
#Use range() to create 30 aliens
aliens = []     #Create an empty list

#Create 30 green aliens
for alien_number in range(30):                                   #loop 30 times
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} #Create a new alien with each loop
    aliens.append(new_alien)                                     #Add the new alien to our list

#Show the first five aliens
for alien in aliens[:5]:                                         #Loop through the first 5 aliens
    print(alien)
print("_________________________")

#Show how many aliens we've created
print(f"Total number of aliens: {len(aliens)}")

#Changing the first three aliens to yellow
for alien in aliens[:3]:            #loop through the only three times
    if alien['color'] == 'green':   #check of alien is green
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'medium'

#Show the first 5 aliens again
for alien in aliens[:5]:
    print(alien)
print("________________________")
