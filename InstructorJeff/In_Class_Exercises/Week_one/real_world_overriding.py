#real world example of method overriding
# The last method defined in the class will override the previous ones.
# In Python, method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
class Animal:
    
    def sound(self):
        print("All animals make a sound")
        
class Dog(Animal):
    def sound(self):
        print("Bark")
        
class Cat(Animal):
    def sound(self):
        print("Meow")
        
#create instances of the subclasses
dog = Dog()
cat = Cat()
#call the overridden method
dog.sound()  # Output: Bark
cat.sound()  # Output: Meow