Shoes ={
    "brand": "Nick",
    "color": "black",
    "size": 40,
}
#print the shoe size
print(Shoes["size"])
print("\n")

#change value
Shoes["brand"] = "Adidas"
print(Shoes["brand"])
print("\n")


#add key-value pair
Shoes["type"] = "sneakers"
print(Shoes)
print("\n")

#return keys
print(Shoes.keys()) #returns the keys as a list
for key in Shoes:   #returns the keys each on a new line.
    print(key)
print("\n")
    
#return values
print(Shoes.values()) #returns the values as a list
for x in Shoes:   #returns the values each on a new line.
    print(Shoes[x])
print("\n")
    
#check if key "size" exists
if "size" in Shoes:
    print("yes,size exists")
else:
    print("no,size does not exist")
print("\n")
    
#loop through the dictionary and print each key-value pair
for key, value in Shoes.items():
    print(key, ":", value)
print("\n")


#remove color from the dictionary
Shoes.pop("color")
print(Shoes)
print("\n")

#empty the dictionary
Shoes.clear()
print(Shoes)
print("\n")


#copy the dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
}
Shoes_copy = Shoes.copy()
print(Shoes_copy)
print("\n")

#nested dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40,
    "details": {
        "type": "sneakers",
        "price": 100,
        "stock": 50
    }
}
print(Shoes["details"]["type"])
print("\n")