"""_If Statements_: Allows you to examine the current state of a program & respond appropriately.
        1. Conditional tests allows you to check any condition of interest.
        2. If statements can only be evaluated as True or False
"""

epl_champions = ['man city', 'liverpool', 'chelsea', 'man united', 'arsenal']

for team in epl_champions:
    if team == 'man city':
        print(team.upper()) #check if the team is 'man city'
    else:
        print(team.title())
        
#Conditional Tests ~ Evaluates to True or False
europe_champions = 'Real Madrid'
europe_champions == 'Real Madrid' #This evaluates to True
europe_champions == 'Liverpool'   #This evaluates to False
