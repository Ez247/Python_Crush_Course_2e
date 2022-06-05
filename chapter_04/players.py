"""_Working with part of a list_: You can work with a specific group of items in a list. Python calls this slicing.
"""
nba_players = ['LeBron', 'Curry', 'KD', 'Giannis', 'Westbrook', 'Klay', 'Dame', 'Embid', 'Ja', 'Luka']

#Slicing a list - Specify the index of the first and last element you want to work with
#Print the first four players in our list
print(nba_players[0:4])

#Print the first five players on the list
print(nba_players[:5]) #Start at index 0 and stop at index 4. Index 5 is not inclusive.

#Print the rest of the list starting with KD
print(nba_players[2:])

#Using negative index
#Print the last 3 players in out list
print(nba_players[-3:])

#Looping through a slice
nba_players = ['LeBron', 'Curry', 'KD', 'Giannis', 'Westbrook', 'Klay', 'Dame', 'Embid', 'Ja', 'Luka']
print("Here are the first three player when I think of the current NBA:")
for player in nba_players[:3]: #loop through only the 1st three names
    print(player.title())