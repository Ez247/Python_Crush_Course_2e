"""_if Statements_:  
        1. Several differents kinds of if statement exist depending on the number of conditions we need to test.
        2. Simple if statement ~ has one test and one action  
        3. Indentation plays the same role in if statements as it did in for loops     
        4. If-else statement ~ the else statement defines an action or set of actions that are executed when
                                the conditional test fails.
"""
#Simple if statement
if conditional_test:  
    do something
    
#Test if someone is old enough to vote
age = 19
if age >= 18:   #Check whether the value of age is greater than or equal to 18.
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
    
#If-else statements examples
age = 17
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')