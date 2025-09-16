"""
Bank Customer Queue System
This program helps a bank manage customer queues by:
- Taking customer names and assigning them sequential ID numbers starting from 1
- Storing customers in order of arrival
- Allowing staff to look up customers by their queue number
- Showing who is ahead in the queue
"""

customers = {}
next_id = 1

while True:
    print("\n1. Add customer")
    print("2. Find customer by number")
    print("3. Show all customers")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        name = input("Enter customer name: ")
        if name.strip(): # Ensure name is not empty
            customers[next_id] = name
            print(f"{name} got number {next_id}")
            next_id = next_id + 1
        else:
            print("Customer name cannot be empty.")
    
    elif choice == "2":
        try:
            number = int(input("Enter customer number: "))
            customer_name = customers.get(number)
            if customer_name:
                print(f"Number {number}: {customer_name}")
            else:
                print(f"No customer found with number {number}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    elif choice == "3":
        if not customers:
            print("The queue is currently empty.")
        else:
            print("Current queue:")
            for num, name in sorted(customers.items()):
                print(f"Number {num}: {name}")
    
    elif choice == "4":
        print("Exiting the system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")