#set of 3 beverages
beverages = {"coffee", "tea", "juice"}
print("My beverages:", beverages)
print("\n")


#adding 2 more beverages
beverages.add("water")
beverages.add("soda")
print("More beverages:", beverages)
print("\n")

#checking for microwave
mySet = {"oven", "microwave", "kettle","refrigerator"}
if "microwave" in mySet:
    print("Microwave is present")
else:
    print("Microwave is not present")
print("\n")

#remove kettle
mySet.remove("kettle")
print("After removing kettle:", mySet)
print("\n")

#loop through the set
print("Looping through the set:")
for x in mySet:
    print(x)
print("\n")

#adding a set and a list
mySet = {"oven", "microwave", "kettle","refrigerator"}
myList=["banana", "apple"]
combinedSetAndList = mySet.union(myList)
print("Combined set:", combinedSetAndList)
print("\n")

#joining two sets
ages = {20, 30, 40}
first_names ={"Selina","Martin","Paul"}
combinedSets = ages.union(first_names)
print("Combined set:", combinedSets)