"""_Letting the user choose when to quit_:
        0. Have to define a quit value
"""

#Example
prompt = "\nTell me something, and I will repeat it back to you: " #define a prompt
prompt += "\nEnter 'quit' to end the program. "

message = ""                    #set the variable message to track user input
while message != 'quit':        #execute as long as user input is not 'quit'
     message = input(prompt)
     
     if message != 'quit':
        print(message)
        
"""_Using a flag_;
        0. Acts as a signal to the program.
        1. One variable is used to determine whether or not the entire program is active.
        2. We write our program to run while the flag is set to True and to stop running 
           when flag is set to False.
        3. As a result our overall while statement needs to check only one condition:
            a. Whether or not the flag is currently True.        
"""

#Using flag with the above program
active = True                  #set the variable to True
while active:
    message = input(prompt)
    
    if message == 'quit':     #check the value of the user input
        active = False
    else:
        print(message)