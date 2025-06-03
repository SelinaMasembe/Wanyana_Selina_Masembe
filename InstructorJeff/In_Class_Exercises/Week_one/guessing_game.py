#generate a random number between 1 and 10 and ask the user to guess it
import random
num = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
#while the guess is not equal to the number, keep asking for a guess 
while guess != num:
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")    
    guess = int(input("Guess a number between 1 and 10: "))
    
print("Congratulations! You guessed the number.")