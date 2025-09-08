"""
A simple ATM simulator which starts with a balance of 1000
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
        amount = input("Enter deposit amount: ")
        if amount.isdigit():
            amount = int(amount)
            balance += amount
            print(f"Deposit successful! New balance: ${balance}")
        else:
            print("Invalid amount.")
    elif choice == "3":
        amount = input("Enter withdrawal amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount <= balance:
                balance -= amount
                print(f"Transaction successful! New balance: ${balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount.")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please choose again.")