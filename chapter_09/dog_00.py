"""Classes:
    0. Object-oriented programming is one of the most effective approaches to writing software.
    1. In OOP we write classes and create objects based on these classes.
    2. A class defines the general behavior a whole category of objects can have.
    3. Making an object from a class is called instantiation, we work with instances of a class.
"""


"""Creating and using a class:
        0. We can model almost anything using classes.    
"""
#Create a class, Dog, that represents a dog.
#Define a class called Dog
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age =  age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in responnse to a command."""
        print(f"{self.name} rolled over!")
        
print("\n________________________")
        
"""Making an instance from a class"""
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

"""Accessing Attributes:
    0. Use the .dot notation, eg my_dog.name to access the value of my_dog's attribute name.
"""
print("\n_______________________")

"""Calling Methods"""
#Make the dog sit and roll over
my_dog.sit()
my_dog.roll_over()

"""Creating Multiple Instances:
    0. We can create as many instances from a class as we need.
"""
print("\n_______________________")

#Create a second dog
his_dog = Dog('Snoop', 10)
her_dog = Dog('Kevin', 2)

print(f"My dog's name is {his_dog.name}.")
print(f"My dog is {his_dog.age} years old.")
his_dog.sit()

print("\n_______________________")

print(f"My dog's name is {her_dog.name}.")
print(f"My dog is {her_dog.age} years old.")
her_dog.sit()

