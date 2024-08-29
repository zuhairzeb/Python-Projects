import time
# Show card insertion message
print("Insert your card.")
time.sleep(2)

# Set up ATM password and balance
password = 1234
balance = 5000

# Check user PIN
while True:
    pin = input("Enter 4-digit PIN: ")
    if pin == str(password):
        break
    print("Incorrect PIN, try again.")

# ATM menu loop
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = input("Enter amount to withdraw: ")
        try:
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                print("You withdrew:", amount)
                print("New balance:", balance)
            else:
                print("Not enough funds.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "3":
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")