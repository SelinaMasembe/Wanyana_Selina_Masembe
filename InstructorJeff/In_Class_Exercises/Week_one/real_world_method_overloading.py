#real world example of method overloading
# The last method defined in the class will override the previous ones.

"""
 To achieve method overloading in Python, we can use default arguments or variable-length arguments.

what are variable-length arguments?
 Variable-length arguments allow a function to accept any number of arguments.
 In Python, this is done using the `*args` syntax, which collects all additional positional arguments into a tuple.
 This allows the function to handle a variable number of inputs without needing to define multiple methods with the same name. 
 
 what are default arguments?
 Default arguments allow a function to have optional parameters that can be set to a default value if not provided by the caller.
"""

#default arguments: you can only enter the number of arguments in the method signature or less
                   #you cannot have more.
class Calculator:
    
    def add(self, a, b=0, c=0):
        result = a + b + c  
        print('The result of addition is:', result)
    
    

adv_calc = Calculator()
adv_calc.add(5, 0) 
adv_calc.add(2,3,4) #max
print("\n")


#variable length arguments:can enter any number of arguments
class MyCalculator:
    
    def add(self,*args):
        result =sum(args)
        print("The sum is:",result)
        
cal = MyCalculator()
cal.add(1, 2, 3)  
print("\n")

#multiple dispach
class MultiDispatchCalculator:
    
    from multipledispatch import dispatch
    
    @dispatch(int,int)
    def add(a,b):
        result = a + b
        print("The sum of 2 integers is:", result)
        
    @dispatch(float,float,float)
    def add(a,b,c):
        result = a+b+c
        print("The sum of 3 floats is:",result)
        
my_obj = MultiDispatchCalculator()
my_obj.add(1,2)
my_obj.add(1.5,1.5,1.5)
print('\n')
    


