"""_Defining a Function_:
        0. Use the key word def ~ informs Python that we are defininf a function.
        1. A function call tells Python to execute the code in the function. 
        2. To call a function ~ write the name of the function followed by any necessary information in the ().
"""

#Define a function called greet_user()
def greet_user():
    """Display a Simple greeting."""
    print("Hello!")
    
greet_user()

"""Passing Information to a Function"""
#Pass a username in our function
def greet_user(username):
    """Display a Simple greeting."""
    print(f"Hello, {username.title()}!")
    
greet_user('james')

"""_Arguments and Parameters_:
        0. In the above examples:
            a. we define a greet_user() function to require a value for the variable username.
            b. The variable username in our function is an example of a parameter ~ a piece of information
                the function needs to do its job.
            c. The value 'james' in our function is an example of an argument ~ a piece of information that is
                passed from a function call to a function.
"""