x=("samsung","iphone","tecno","redmi")

#output my favorite phone
print("My favorite phone is:", x[1])
print("\n")

#negative indexing to print second last item
print("The second last phone is:", x[-2])
print("\n")

#update iphone to itel
#recall that tuples are immutable
"""
1.Convert the tuple to a list
2.Update the list
3.Convert the list back to a tuple
"""
my_list = list(x)
my_list[1] = "itel"
x =tuple(my_list)
print("Updated tuple with itel instead of iphone:", x)  
print("\n")

#add Huawei to the tuple
"""
Tuples dont have append method
1.Convert the tuple to a list
2.Add the item to the list
3.Convert the list back to a tuple
"""
my_second_list = list(x)
my_second_list.append("Huawei")
x=tuple(my_second_list)
print("Updated tuple with Huawei:", x)
print("\n")

#loop through the tuple
print("Looping through the tuple:")
for phone in x:
    print(phone)
print("\n")

#delete first item
"""
1.Convert the tuple to a list
2.Delete the first item 
3.Convert the list back to a tuple
"""
my_third_list = list(x)
del my_third_list[0]
x=tuple(my_third_list)
print("Updated tuple after deleting first item:", x)
print("\n")

#using tuple constructor
ugandan_cities = tuple(("Kampala", "Entebbe", "Jinja", "Mbarara"))
print("Tuple of Ugandan cities:", ugandan_cities)
print("\n")



#unpacking tuples
#unpacking is the process of extracting values from a tuple and assigning them to variables
#syntax: variable1, variable2, variable3 = tuple

*city_1, city_2, city_3 = ugandan_cities
print("Cities in Buganda:", city_1)
print("City in Busoga:", city_2)
print("City in Ankole:", city_3)
print("\n")

#range of 2nd,3rd and 4th cities 
print("The range of 2nd,3rd and 4th cities is:", ugandan_cities[1:4])
print("\n")

#two tuples to join
first_names = ("Selina", "Martin", "Paul")
second_names = ("Masembe", "Mpagi", "Bwogi")
combined_tuples = first_names + second_names
print("Combined tuples:", combined_tuples)
print("\n")

#tuple of colors multiplied by 3
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print("Multiplied tuple of colors:", multiplied_colors)
print("\n")

#return number of 8(s) in the tuple
this_tuple = (1,3,7,8,7,5,4,6,8,5)
count_of_8 = this_tuple.count(8)
print("The number of 8(s) in the tuple is:", count_of_8)
print("\n")