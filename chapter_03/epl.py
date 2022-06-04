"""_List_[]: A collection of items in a particular order. 
        1. Lists allows you to store sets of information in one place.
        2. You can put anything you want into a list. Items don't have to be related.
        3. One of Python's most powerful features.
"""
#Creating a list[]
epl_teams = ['arsenal', 'chelsea', 'liverpool', 'man city', 'man united', 'tottenham']
print(epl_teams)

#Accessing Elements in a List ~ use index which position starts at 0 and not 1
#Let's pull the 3rd team on the list
print(epl_teams[2].title())

#Let's pull the last item on the list using negative index[-1]
print(epl_teams[-1].title())

#Using individual values from a list ~ use f-strings to create a message based on the list
message = f"{epl_teams[3].title()} are the 2021/22 Premier League Champions."
print(message)
