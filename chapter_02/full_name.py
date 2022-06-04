"""_f strings_: f stands for format, & you can do a lot with f strings. 
        1. You can use f-strings to compose complete message using the below statements.
        2. f-strings were first introduced in Python 3.6
"""
first_name = 'kevin'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print('Hello, ' + full_name)
print(f"Hello, {full_name.title()}!") #capitalize the first letters on the name

