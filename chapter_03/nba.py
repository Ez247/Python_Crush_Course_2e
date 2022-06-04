"""_More on Lists_: Changing, Adding, and Removing Elements
            1. Syntax for modifying and accessing an element in a list is similar.
            2. To change an element, use the name of the list followed by the index. 
"""

#List of top NBA teams
nba_teams = ['warriors', 'celtics', 'lakers', 'bulls', 'suns', 'nets', 'bucks', '76ers', 'grizzlies', 'jazz']
print(nba_teams)

#Modifying elements in a list
nba_teams[2] = 'heat' #Change or replace the lakers with the heat
print(nba_teams)

#Adding Elements to a list .append()
nba_teams.append('raptors') #Add the raptors to the list
print(nba_teams)

#Inserting Elements into a list .insert()
nba_teams.insert(5, 'nuggets') #Add nuggets before the nets
print(nba_teams)

#Removing Elements from a list, del statement(use if position of the element is known)
del nba_teams[10] #Remove the jazz from the list
print(nba_teams)

#Removing an element usisng the pop() method
#Lets you remove the last item in a list and let's you work with that item after removing it.

popped_nba_teams = nba_teams.pop() #Remove the last team from the list
print(nba_teams)       #Print the original nba teams list 
print(popped_nba_teams) 

#Remove an item by value remove()
nba_teams.remove('grizzlies') #Remove grizzlies from the list
print(nba_teams)