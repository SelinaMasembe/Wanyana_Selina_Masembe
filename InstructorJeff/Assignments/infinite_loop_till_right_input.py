#Write a program to handle errors.
"""
It should ask a user for two numbers and divide them.
Use an infinite loop to keep asking for input until the user provides valid numbers.
"""

#once an exception is thrown, the program will not terminate.
#the respective exception will be caught and handled.
#the progrsm then asks for the input again,starting from the beginning.
def divide_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
        except ValueError: #ValueError is raised when the input is not a number,eg "abc" instead of a number
            print("Invalid input. Please enter valid numbers.")
            print("\n")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
            print("\n")
        else:
            print("The result of dividing", num1, "by", num2, "is:", result)
            break

#calling function
divide_numbers()
    