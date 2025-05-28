#Loops are used to repeat a block of code multiple times if a condition is true.

#            for loop
print("for loop:")
for x in range(6):
  print(x)
  
#The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.


#           while loop
#used to execute a set of statements as long as a condition is true
i = 1
print("while loop:")
while i < 6:
  print(i)
  i += 1
  
  
#                       break statement
#used to exit a loop even if the while condition is true.

#Odd numbers less than 7
print("break statement:")
count = 1
while count < 10:
  if count == 7:
    break
  print(count)
  count += 2
  
  #                      continue statement
#used to skip the current iteration of a loop and continue with the next iteration.

j = 0
print("continue statement:")
while j < 10:
  j += 1
  if j == 5:
    continue
  print(j)
  