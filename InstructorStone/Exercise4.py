                          #STRINGS
#1.join a string and a number
#and print them in the same line 
x= "Hi"
y= 5
print(x,y)

#2.Remove spaces from the start and end of a string
#and remove all spaces from a string
txt=" Hello, Uganda "
remove_startend_spaces = txt.strip()
print(remove_startend_spaces)


remove_all_spaces = txt.replace(" ", "")
print(remove_all_spaces)

#3.To uppercase a string
uppercase_string = txt.upper()
print(uppercase_string)

#4.Replace a string with another string
replace = txt.replace("U", "V")
print(replace)

#5.Range of characters in the 2nd, 3rd and 4th position 
y = "I am proudly Ugandan"
range_of_characters = y[1:4]  #prints till character before the one in the 4th position.
print(range_of_characters)

#6.Correcting a string with double quotes

#x="All "Data Scientists" are cool"
corrected_string = 'All "Data Scientists" are cool'
print(corrected_string)
