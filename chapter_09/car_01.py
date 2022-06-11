"""Working with Classes and Instances:
        0. We will first want to modify the attributes associated with  particular instance.
        1. We can do this directly or we can write methods that update attributes in specific ways.
"""

"""The car class"""
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initilize attributes to describe a car."""
        self.make = make
        self.model =  model
        self.year = year
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())     

"""Setting a default value for an attribute
        0. Attributes can be defined without being passed in as parameters.
        1. We assign them a default value in the __init__() method.
"""
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initilize attributes to describe a car."""
        self.make = make
        self.model =  model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statment showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
          
    def update_odometer(self, mileage):
            """set the odometer reading to the given value.
               Rejec the change if it attempts to roll the odometer back.
            """
            self.odometer_reading = mileage
        
my_new_car = Car('jaguar', 'xj6', 1992)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
        
"""Modifying attribute values:
        0. This can be done in three ways:
            i. You can change the value directly through an instance.
           ii. Set the vale through a method
          iii. Increment the value (add a certain anount to it) through a method  
"""    
"""Modifying an attribute's value directly.
        0. The simplest way to modify an attributes value.
"""
my_new_car.odometer_reading =  23
my_new_car.read_odometer() 

"""Modifying an attribute's value through a method.
        0. You pass a new value to a method that handles the updating internally.
"""
my_new_car.update_odometer(50)   
my_new_car.read_odometer()