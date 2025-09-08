"""
A simple ATM simulator which starts with a balance of 1000
It allows the user to check balance, deposit, withdraw, and exit.
It is a simple text-based interface.
"""

balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your balance is: ${balance}")
    elif choice == "2":
        try:
            amount = input("Enter deposit amount: ")
            amount = int(amount)
            if amount <= 0:
                print("Amount must be positive.")
            else:
                balance += amount
                print(f"Deposit successful! New balance: ${balance}")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "3":
        try:
            amount = input("Enter withdrawal amount: ")
            amount = int(amount)
            if amount <= 0:
                print("Amount must be positive.")
            elif amount <= balance:
                balance -= amount
                print(f"Transaction successful! New balance: ${balance}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")