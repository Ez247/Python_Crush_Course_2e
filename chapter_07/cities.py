"""_Using break to Exit a loop_:
        0. To exit a while loop, use the break statement.
        1. The break statement directs the flow of your program:
                a. Use it to control which lines of code are executed and which aren't.
"""

#Example
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        