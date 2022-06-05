"""_The if-elif-else chain_: At times you may need to test more than two possible conditions.
            1. Python's if-elif-else chain:
                a. Runs each conditional test in order until one passes.
                b. When a test passes, the code is executed and Python skips the rest of the tests.
            2. You can use as many elif blocks as you like.
            3. Python does not require an else block at the end of an if-elif chain, but its useful.
"""

#If-elif-else chain example
"""_Consider an amusement park_:
        1. Admission for anyone under age 4 is free.
        2. Admission for anyone between the ages of 4 and 18 is $10.
        3. Admission for anyone age 18 or older is $20.
"""

age = 20

if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $10')
else:
    print('Your admission cost is $20.')
       
# A more concise way to write this code
age = 3

if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 20

print(f"Your admission cost is ${price}.")
    
#Using multiple elif Blocks 
#The amusements implements a 0% discount for seniors (age 65 and older), price $10

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 20
else:
    price = 12
    
print(f"Your admission cost is ${price}.")
    
#Omitting the else block ~ Sometimes an else block is useful
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 20
elif age >= 65:
    price = 12
    
print(f"Your admission cost is ${price}.")