"""
ERROS
   These occur when a program encounters an unexpected situation that it cannot handle.
   
   TYPES OF ERRORS
    1. Syntax Errors: These occur when the code is not written in a way that Python can understand.
    2. Runtime Errors: These occur when the code is syntactically correct but fails during execution.
    3. Logical Errors: These occur when the code runs without errors but produces incorrect results.
    
    HANDLING ERRORS 
       try,except,else,finally
    
    1. Try-Except Blocks:
         - Used to catch and handle exceptions.
         - Prevents the program from crashing.
    2. Finally Block:
            - Always executes, regardless of whether an exception occurred or not.
            - Used for cleanup actions (e.g., closing files).   
    3.Else Block:
            - Executes if no exceptions were raised in the try block.
    4.Except Block:
            - Used to handle "SPECIFIC" exceptions.
            - Can be used to catch multiple exceptions.
"""

try:
    quotient = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("The result is:", quotient)
finally:
    print("This block always executes, regardless of exceptions.")
print("\n")