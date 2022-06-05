"""_Numerical Comparisons_: This is straightforward.
        1. Test for equality
        2. Use AND to test for multiple conditions (All conditions must evaluate to True)
        3. Use OR to test for multiple conditions (Only one condition has to be True)
"""

age = 18
age == 18 #This checks if age is equal to 18 and evaluated to True

#Check if a given number is incorrect
answer = 17

if answer != 42:
    print('That is not the correct answer. Please try again!')
    
#Checking multiple conditions
user_0 = 22
user_1 = 18
(user_0 >= 21) and (user_1 >= 21) #Evaluates to false since only one condition is met and True

user_1 = 24
(user_0 >= 21) and (user_1 >= 21) #Evaluates to True since both conditions are met and True

#Using OR to check multiple conditions
user_0 = 22
user_1 = 18
(user_0 >= 21) or (user_1 >= 21) #Evaluates to True since one conditions is met and True

