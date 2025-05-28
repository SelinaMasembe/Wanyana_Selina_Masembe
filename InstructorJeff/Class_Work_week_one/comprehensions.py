#List and Dictionary Comprehensions

#list comprehension is a concise way to create lists in Python.
# It consists of "square brackets" containing an expression followed by a for clause, then zero or more for or if clauses.


#using for loops in list comprehensions
#for squares
squares = []
for x in range(10):
    squares.append(x**2)
    print(squares)
    
#using list comprehensions
squares = [x**2 for x in range(10)]
print(squares)

#using if statements in list comprehensions
#for even squares
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x**2)
        print(even_squares)
        
#using list comprehensions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)





#dictionary comprehension is a concise way to create dictionaries in Python.
# It consists of "curly braces "containing an expression followed by a for clause, then zero or more for or if clauses.
#using for loops in dictionary comprehensions
#for squares
squares = {}
for x in range(10):
    squares[x] = x**2
    print(squares)
    
#using dictionary comprehensions
squares = {x: x**2 for x in range(10)}
print(squares)