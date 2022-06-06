"""_Using a while loop with Lists and Dictionaries_:
        0. Allows you to collect, store, and organize lots of input to examine and reporrt on later.
"""

#Moving items from one list to another
#Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'bryan', 'owen']              #A list of unconfirmed users
confirmed_users = []                                        #An empty list of confirmed_users

#Verifyeach user unotl there are no more inconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:                                    #While loop runs as long as  uniconfirmed list isn't empty
    current_user = unconfirmed_users.pop()                  #Remove unverified users one at time, staring with owen.
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)                    #Add current users to our confirmed users list.
    
#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())