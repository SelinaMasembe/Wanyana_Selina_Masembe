#LISTS
#1.a list of 5 items, print 2nd item
names= ["Selina", "Rose", "Martin", "Isaac", "Paul"]
print(names[1]) # Jane

#change value of first item
names[0] = "Mike"
print(names[0]) 

#add 6th item to list
names.append("Mary")
print(names)

#add Bathel as 3rd item
names.insert(2, "Bathel")
print(names)

#remove 4th item
#names.remove("Isaac")
names.pop(3)
print(names)

#negative indexing to print last item
print(names[-1]) # Mary

#another list with 7 items
fruits = ["banana", "apple", "orange", "grape", "kiwi", "mango", "peach"]
#print 3rd to 5th items
print(fruits[2:6]) 

#list of countries
countries = ["USA", "Canada", "Mexico", "UK", "Germany", "France", "Italy"]
#making a copy of the list
countries_copy = countries.copy()
print(countries_copy)

#loop through the list and print each country
for country in countries:
    print(country)
    
#animal list
animals = ["ant", "cat", "elephant", "tiger", "lion"]
#sort the list in descending order
animals.sort(reverse=True)
print(animals)

#ascending order
animals.sort()
print(animals)

#animals starting with 'a'
animals_starting_with_a = [animal for animal in animals if animal.startswith('a')]
print(animals_starting_with_a)

#combine two lists
first_names= ["Selina", "Mable", "Paul"]
second_names= ["Rose", "Martin", "Isaac"]
combined_names = first_names + second_names
print(combined_names)