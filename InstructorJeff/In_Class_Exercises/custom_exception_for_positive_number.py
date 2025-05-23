#raise a custom exception if the number is  positive
try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("The number is not positive.")
except ValueError as e:
    print(e)
else:   
    print("The number is positive.")
finally:
    print("Execution completed.")