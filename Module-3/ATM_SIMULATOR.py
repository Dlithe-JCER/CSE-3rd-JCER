print("----- Welcome to Python ATM -----")

# Initial values
PIN = 1234
balance = 1000.0
transactions = []   

for attempt in range(3):
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == PIN:
        print("Login successful!\n")
        break
    else:
        print("Incorrect PIN! Try again.")
else:
    print("Too many incorrect attempts. Your account is locked.")
    exit()


while True:
    print("\n------- ATM MENU -------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Choose an option: ")

    # 1. Deposit
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        
        if amount <= 0:
            print("Invalid amount! Please enter a positive value.")
            continue
        
        balance += amount
        transactions.append(f"Deposited: ₹{amount}")
        print(f"₹{amount} deposited successfully!")

    # 2. Withdraw 
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        
        if amount <= 0:
            print("Invalid amount! Please enter a positive value.")
            continue

        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully!")

    # 3. Check Balance
    elif choice == "3":
        print(f"Your current balance is: ₹{balance}")

    # 4. Transaction History
    elif choice == "4":
        if not transactions:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in transactions:
                print(t)

    # 5. Exit
    elif choice == "5":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid option! Please try again.")
