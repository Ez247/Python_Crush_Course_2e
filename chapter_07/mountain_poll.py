"""_Filling a Dictionary with user input_: 
        0. Make a polling program in which each pass through the loop:
            a. prompts for the participant's name and response.
            b. stores the data we gather in a dictionary
"""

responses = {}

#Set a flag to indicate that polling is active.
polling_active =  True 

while polling_active:
    #prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    #store the response in the dictionary
    responses[name] = response
    
    #Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
        
#Polling is complete. Show results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
