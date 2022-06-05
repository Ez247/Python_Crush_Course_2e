"""_Checking Whether a value is in a list_: 
            1. Sometimes we want to check whether a list contains certain value before taking an action.
            2. Use the keyword in as shown in the first example.        
            3. Other times we want to know if a value does not appear in a list.
            4. Use the keyword not in this situation
"""

#Check whether certain toppings are in the list (use keyword in)
requested_toppings = ['mushroom', 'onions', 'pineapple', 'spinach']
'mushroom' in requested_toppings    #Check for the existence of 'mushroom' in the list requested_toppings
'pepperoni' in requested_toppings   #Check for the existence of 'pepperoni' in the list requested_toppings

#Checking whether a value is not in a list (use keyword not)
banned_users = ['andrew', 'carolina', 'david', 'smith']
user = 'marie'

if user not in banned_users:  #if user value is not in the list banned_users
    print(f"{user.title()}, you can post a response if you wish.")
    
#Boolean Expressions ~ Another name for a conditional test (True or False)
game_active = from 
can_edit = False
