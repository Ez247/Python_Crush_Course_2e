"""_Copying a list_: 
        1. You can make a slice that includes the entire original list by omitting the first and last indexes([:])       
"""
my_food = ['pizza', 'falafel', 'carrot cake']

#Make a copy of the above list
friends_food = my_food[:]

print(my_food)
print(friends_food)

#Add a new food to my list
my_food.append('cannoli')

#Add a new food to my friends list
friends_food.append('ice cream')

print(my_food)
print(friends_food)