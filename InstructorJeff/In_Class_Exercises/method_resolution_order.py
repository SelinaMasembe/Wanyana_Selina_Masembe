#method resolution order (MRO) is the order in which Python looks for a method in a hierarchy of classes.
# MRO is important in multiple inheritance scenarios, where a class inherits from more than one parent class.
# Python uses the C3 linearization algorithm to determine the MRO, which ensures a consistent and predictable order of method resolution.
# The MRO can be viewed using the `__mro__` attribute or the `mro()` method of a class.
class A:
    def method(self):
        print("Method in class A")
        
class B(A):
    def method(self):
        print("Method in class B")
        
class C(A):
    def method(self):
        print("Method in class C")
        
class D(B, C):
    def method(self):
        print("Method in class D")
        
# Display the method resolution order
print(D.__mro__)
# or using the mro() method
print(D.mro())

# Create an instance of class D and call the method
print("\n")
print("Calling method from class D:")
d_instance = D()
d_instance.method()  # This will call the method in class D due to MRO