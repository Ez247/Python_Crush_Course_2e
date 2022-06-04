"""_Organizing a List_: Often your list will be created in an unpredictable order.
"""

epl_teams = ['arsenal', 'chelsea', 'liverpool', 'man city', 'man united', 'tottenham', 'everton', 'fulham', 'aston villa']

#Sorting a list permanently with the sort() method
epl_teams.sort() #sort the list alphabetically and change the order of the list permanently
print(epl_teams)

#Reverser sort
epl_teams.sort(reverse=True) #Reverse the order of the list
print(epl_teams)

#Sorting a list Temporarily with the sorted() function
print(sorted(epl_teams)) #Lets you display your 1st list in a particular order but doesn't affect the list.

#Finding the length of a list, len() function
epl_teams = ['arsenal', 'chelsea', 'liverpool', 'man city', 'man united', 'tottenham', 'everton', 'fulham', 'aston villa']
print(len(epl_teams))

