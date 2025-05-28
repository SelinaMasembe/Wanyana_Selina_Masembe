#objects, classes, 
"""
KEY CONCEPTS:
inheritance, polymorphism, abstracion,encapsulation
"""

#inheritance

#child or derived class or sub class: inherits all the properties and methods of the parent class
"""
WHY inheritance?
1. Code Reusability: Child classes can reuse methods and properties of parent classes, reducing code duplication.
2. Extensibility: Child classes can extend or modify the behavior of parent classes, allowing for more specialized functionality.
"""

#parent or base class or super class
class Animal:
    def make_sound(self):
        print("Some generic animal sound") 
        
#child or derived class or sub class
class Cat(Animal):
    def speak(self):
        print("Meow")
        
cat1 = Cat()
cat1.make_sound()  # Inherited method from Animal class
cat1.speak()       # Method from Cat class
print("\n")

#multiple inheritance is allowed in python
class Father:
    def skills(self):
        print("Father's skills: Carpentry, Plumbing")

class Mother:
    def skills(self):
        print("Mother's skills: Cooking, Sewing")
        
class Child(Father, Mother):
    def skills(self):
        # Calling skills from both Father and Mother classes
        Father.skills(self)
        Mother.skills(self)
        print("Child's skills: Painting, Drawing")
        
        
child = Child()
child.skills()  # Calls the skills method from Child class
print("\n")


# Polymorphism
# Polymorphism allows methods(same method) to do different things based on the object it is acting upon, even if they share the same name.
class Bird:
    def fly(self):
        print("Birds fly in the sky")
        
class Eagle(Bird):  #sub class of Bird
    def fly(self):
        print("Eagles soar high in the sky")
        
class Sparrow(Bird):  #sub class of Bird
    def fly(self):
        print("Sparrows flutter around quickly")
        
def flight_test(bird):
    bird.fly()  # Calls the fly method of the specific bird object passed to it 
        
#creating objects of the subclasses
eagle = Eagle()
sparrow = Sparrow()

flight_test(eagle)    # Output: Eagles soar high in the sky
flight_test(sparrow)  # Output: Sparrows flutter around quickly
print("\n")


#Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object.

"""
1. use @abstractmethod decorator to define abstract methods in an abstract class
2.import ABC from abc module
3. Create a class that inherits from ABC
from abc import ABC, abstractmethod
"""

from abc import ABC, abstractmethod

"""
1.You cannot create an instance of an abstract class (Vehicle in this case).
2.You must implement all abstract methods in the derived class (Car in this case) to create an instance of that class.

ie: vehicle = Vehicle()  # This will raise an error because Vehicle is abstract
"""

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method, no implementation here
    
#class Car inherits from Vehicle and provides implementation for the abstract method
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
        
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
        
# Creating instances of Car and Bike
car = Car()
bike = Bike()
car.start_engine()  # Output: Car engine started
bike.start_engine()  # Output: Bike engine started
print("\n")
        
