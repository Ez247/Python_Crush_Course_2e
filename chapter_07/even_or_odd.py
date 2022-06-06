"""_The Modulo Operator (%)_:
        0. A useful tool for working with numerical information.
        1. It divides a number and returns the remainder.
        2. It doesn't tell you how many times a number fits into another.
"""

#Examples
4 % 3   #Evaluates to 1
5 % 3   #Evaluates to 2
6 % 3   #Evaluates to 0
7 % 3   #Evaluates to 1

#Determine if a given number is even or odd
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number is {number} is even.")
else:
    print(f"\nThe number is {number} is odd.")