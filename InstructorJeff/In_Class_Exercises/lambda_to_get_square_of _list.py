my_list =[1, 2, 3, 4, 5]
# Using lambda function to get the square of each element in the list
squared_list = list(map(lambda x: x**x, my_list))
print("The square of the list is:", squared_list)
print("\n")

#                              map function
#map function applies a function to all the items in an input list
#map(function, iterable)