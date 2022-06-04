"""_List Comprehensions_: Allows you to generate a list in just one line of code.
                1. It combines the for loop and the creation of the new element into one line.
                2. Automatically appends each new element.
"""

#Build a list with the square of numbers in the range 1 to 10.
squares = [value**2 for value in range(1, 11)]
print(squares)

#Make a list of 1 through 1 million
numbers = list(range(1, 1000001))

#Find the mininum number in our list
print(min(numbers))

#Find the maximum number in our list
print(max(numbers))

#Find the sum of our list
print(sum(numbers))

#A list of odd numbers between 1 and 20
odd_numbers = []             #make an empty list and save it under the variable name odd_numbers
for num in range(1, 21, 2):  #for every number between 1 and 21 starting with 1, skip the next number
    odd_numbers.append(num)  #Add the numbers to our empty list
print(odd_numbers)

#A concise way to make the above list
odd_numbers2 = list(range(1, 21, 2))
print(odd_numbers2)

#An even more concise way to achieve this is using list comprehension
odd_numbers3 = [num for num in range(1, 21, 2)]
print(odd_numbers3)

#A list of multiples of 3 from 3 to 30 
multiples = []
for num in range(1, 31):
    multiple = num * 3
    multiples.append(multiple)
print(multiples)

#A more concise code for multiples of three
multiples1 = [num * 3 for num in range(1, 31)]
print(multiples1)

#A list of the first 10 cubes
cubes = []
for cube in range(1, 11):
    cube = cube ** 3
    cubes.append(cube)
print(cubes)

#A more concise list of the first 10 cubes ~ Use list comprehension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)