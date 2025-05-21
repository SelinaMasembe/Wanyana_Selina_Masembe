#Nested if-else statements for a movie ticket booking system
age= int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
    has_ticket = input("Do you have a ticket? (yes/no): ").strip().lower()
    if has_ticket == "yes":
        print("You can enter the movie.")
    else:
        print("You cannot enter the movie without a ticket.")
else:
    print("You are not old enough to watch this movie.")
