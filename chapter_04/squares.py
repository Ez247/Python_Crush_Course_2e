"""_More on lists_: You can create almost any set of numbers you want with the range() function
"""

#Get the squares of all numbers between 1 and 10
squares = [] #creates an empty list
for value in range(1, 11):
    square = value ** 2    #square the values in our range function
    squares.append(square) #Append each square value to the list of squares
print(squares)

#A more concise way to write the above code
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#Simple statistics with a list of numbers ~ use the newly created list from above
#Find the minimum number in our list
print(min(squares))

#Find the maximum number in our list
print(max(squares))

#Find the sum of the numbers in our list
print(sum(squares))