#function to get the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#getting factorial of 5
result = factorial(5)
print("The factorial of 5 is:", result)