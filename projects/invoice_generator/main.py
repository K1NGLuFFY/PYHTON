#!/usr/bin/env python3
"""
Invoice Generator - Main Application
A comprehensive invoice generation system using Python
"""

import os
from datetime import datetime
from invoice import Invoice
from invoice_manager import InvoiceManager
from utils import clear_screen, get_user_input

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("       INVOICE GENERATOR")
    print("="*50)
    print("1. Create New Invoice")
    print("2. View All Invoices")
    print("3. Search Invoice")
    print("4. Export Invoice to PDF")
    print("5. Exit")
    print("="*50)

def create_invoice_flow():
    """Interactive flow for creating a new invoice"""
    clear_screen()
    print("\n--- CREATE NEW INVOICE ---")
    
    # Get customer details
    customer_name = get_user_input("Enter customer name: ")
    customer_email = get_user_input("Enter customer email: ")
    customer_address = get_user_input("Enter customer address: ")
    
    # Create new invoice
    invoice = Invoice(customer_name, customer_email, customer_address)
    
    # Add items
    while True:
        print("\n--- ADD ITEM ---")
        description = get_user_input("Item description: ")
        quantity = float(get_user_input("Quantity: "))
        unit_price = float(get_user_input("Unit price: "))
        
        invoice.add_item(description, quantity, unit_price)
        
        add_more = get_user_input("\nAdd another item? (y/n): ").lower()
        if add_more != 'y':
            break
    
    # Set tax rate
    tax_rate = float(get_user_input("Enter tax rate (as percentage, e.g., 18.5): "))
    invoice.set_tax_rate(tax_rate)
    
    # Save invoice
    manager = InvoiceManager()
    invoice_number = manager.save_invoice(invoice)
    
    print(f"\n✅ Invoice created successfully!")
    print(f"Invoice Number: {invoice_number}")
    print(f"Total Amount: ${invoice.calculate_total():.2f}")
    
    # Ask to generate PDF
    generate_pdf = get_user_input("\nGenerate PDF now? (y/n): ").lower()
    if generate_pdf == 'y':
        filename = f"invoice_{invoice_number}.pdf"
        invoice.generate_pdf(filename)
        print(f"PDF generated: {filename}")

def view_all_invoices():
    """Display all saved invoices"""
    clear_screen()
    print("\n--- ALL INVOICES ---")
    
    manager = InvoiceManager()
    invoices = manager.get_all_invoices()
    
    if not invoices:
        print("No invoices found.")
        return
    
    for invoice in invoices:
        print(f"\nInvoice #{invoice['invoice_number']}")
        print(f"Customer: {invoice['customer_name']}")
        print(f"Date: {invoice['date']}")
        print(f"Total: ${invoice['total']:.2f}")
        print("-" * 40)

def search_invoice():
    """Search for a specific invoice"""
    clear_screen()
    print("\n--- SEARCH INVOICE ---")
    
    search_term = get_user_input("Enter invoice number or customer name: ")
    manager = InvoiceManager()
    
    results = manager.search_invoices(search_term)
    
    if not results:
        print("No matching invoices found.")
        return
    
    for invoice in results:
        print(f"\nInvoice #{invoice['invoice_number']}")
        print(f"Customer: {invoice['customer_name']}")
        print(f"Email: {invoice['customer_email']}")
        print(f"Date: {invoice['date']}")
        print(f"Total: ${invoice['total']:.2f}")
        
        view_details = get_user_input("\nView full details? (y/n): ").lower()
        if view_details == 'y':
            display_invoice_details(invoice['invoice_number'])

def display_invoice_details(invoice_number):
    """Display detailed information for a specific invoice"""
    manager = InvoiceManager()
    invoice = manager.get_invoice(invoice_number)
    
    if not invoice:
        print("Invoice not found.")
        return
    
    clear_screen()
    print("\n" + "="*60)
    print(f"INVOICE #{invoice['invoice_number']}")
    print("="*60)
    print(f"Date: {invoice['date']}")
    print(f"\nBILL TO:")
    print(f"Name: {invoice['customer_name']}")
    print(f"Email: {invoice['customer_email']}")
    print(f"Address: {invoice['customer_address']}")
    
    print("\n" + "-"*60)
    print("ITEMS:")
    print("-"*60)
    print(f"{'Description':<30} {'Qty':<10} {'Price':<10} {'Total':<10}")
    print("-"*60)
    
    for item in invoice['items']:
        total = item['quantity'] * item['unit_price']
        print(f"{item['description']:<30} {item['quantity']:<10} ${item['unit_price']:<9.2f} ${total:<9.2f}")
    
    print("-"*60)
    print(f"{'Subtotal':>50} ${invoice['subtotal']:.2f}")
    print(f"{'Tax':>50} ${invoice['tax_amount']:.2f}")
    print(f"{'TOTAL':>50} ${invoice['total']:.2f}")
    print("="*60)

def main():
    """Main application loop"""
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    while True:
        display_menu()
        choice = get_user_input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            create_invoice_flow()
        elif choice == '2':
            view_all_invoices()
        elif choice == '3':
            search_invoice()
        elif choice == '4':
            invoice_num = get_user_input("Enter invoice number to export: ")
            manager = InvoiceManager()
            invoice = manager.get_invoice(invoice_num)
            if invoice:
                from invoice import Invoice as InvoiceClass
                inv = InvoiceClass(
                    invoice['customer_name'],
                    invoice['customer_email'],
                    invoice['customer_address']
                )
                inv.items = invoice['items']
                inv.tax_rate = invoice['tax_rate']
                filename = f"invoice_{invoice_num}.pdf"
                inv.generate_pdf(filename)
                print(f"PDF exported: {filename}")
            else:
                print("Invoice not found.")
        elif choice == '5':
            print("Thank you for using Invoice Generator!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
