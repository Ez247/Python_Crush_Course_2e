"""_The input() function_: How it works
        0. Pauses your program and waits for the user to enter some text.
        1. Once received, Python assigns that input to a varibale to make it convenient.
        3. Input() function takes one argument ~ the prompt
"""

#Example
name = input("Please enter your name: ")
print(f"Hello, {name.title()}!")

"""_Writing Clear Prompt_: At times we will want to write longer prompts
        0. We might want to let the user why we are asking for their input.
        1. We assign our prompt to a variable
        2. Pass that variable to the input() function
"""
prompt = "We can personalize a special message just for you to see if you tell us who you are."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")