"""_syntax error_: This occurs when Python  doesn't recognize a section of your program as 
                    valid Python Code. E.g:
            1. Using an apostrophe within single quotes. 
"""
#This prints since the apostrophe appears inside a set of double quotes.
message = "One of Python's strenghts is its diverse community."
print(message)

#This won't print since the apostrophe appears inside a set of double quotes.
message = 'One of Python's strengths is its diverse community.'
print(message) #This will display an invalid syntax.