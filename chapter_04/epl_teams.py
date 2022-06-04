"""_Loops_: Allows you to do or take the same action multiple times.
        1. Loops are important because they let you automate repetitive tasks.
"""

epl_teams = ['arsenal', 'chelsea', 'liverpool', 'man city', 'man united', 'blackburn', 'leicester']

#Looping through an entire list
for team in epl_teams: #for every team in the list of epl_teams
    print(team.title()) #print the team's name
    
#Doing more work within a for loop
for team in epl_teams:
    print(f"{team.title()}, is among the teams wiht a Premier League title.")