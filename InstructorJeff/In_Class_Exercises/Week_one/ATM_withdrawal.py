#check account balance before withdrawal
# ATM withdrawal program

password = "1234"
balance = 1000

# Get user input for password
user_password = input("Enter your password: ")
# Check if password is correct
if user_password == password:
    #display options
    print("Welcome to the ATM!")
    print("1. Check balance")
    print("2. Withdraw cash")
    print("3. Exit")
    # Get user input for option
    option = int(input("Select an option (1-3): "))
    # Check if option is valid
    if option in [1, 2, 3]:
        if option == 1:
            print("Your balance is: $", balance)
        elif option == 2:
            # Get user input for withdrawal amount
            withdrawal_amount = int(input("Enter the amount to withdraw: "))
            # Check if withdrawal amount is valid
            if withdrawal_amount > 0 and withdrawal_amount <= balance:
                balance -= withdrawal_amount
                print("Withdrawal successful! Your new balance is: $", balance)
            else:
                print("Invalid withdrawal amount.")
        elif option == 3:
            print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid option selected.")
