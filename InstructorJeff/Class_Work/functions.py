#                                   Python Functions
# A function is a reuable block of code that performs a task when called.

"""
WHY FUNCTIONS?
1. Code Reusability: Functions allow you to write code once and reuse it multiple times, reducing redundancy.
2.Organize code
3.Easier to debug
4.Logical structure
"""

def greet_student ():
    print("Hello, Student!")
 
# Call the function
greet_student()   

#PEP8 guidelines:
#Snake case for function names
#Use lowercase letters

#add numbers 

def add_numbers(num1,num2):
    result = num1 + num2
    print("The sum of",num1,"and", num2,"is:", result)
    
add_numbers(5,6)