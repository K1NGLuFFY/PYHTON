#!/usr/bin/env python3
"""
Shop Inventory System - Main CLI Interface
A comprehensive system to track stock, sales, and receipts.
"""

import os
import sys
from datetime import datetime, timedelta
from typing import List, Tuple

from inventory import Inventory, Product, Sale, Receipt

class InventoryCLI:
    """Command-line interface for the inventory system."""
    
    def __init__(self):
        self.inventory = Inventory()
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self, title: str):
        """Display a formatted header."""
        print("=" * 60)
        print(title.center(60))
        print("=" * 60)
    
    def display_menu(self):
        """Display the main menu."""
        self.clear_screen()
        self.display_header("SHOP INVENTORY SYSTEM")
        print("\n1. Product Management")
        print("2. Sales Management")
        print("3. Receipt Management")
        print("4. Reports")
        print("5. Exit")
        print("\n" + "=" * 60)
    
    def product_menu(self):
        """Product management submenu."""
        while True:
            self.clear_screen()
            self.display_header("PRODUCT MANAGEMENT")
            print("\n1. Add New Product")
            print("2. View All Products")
            print("3. Search Products")
            print("4. Update Product")
            print("5. Check Low Stock")
            print("6. Back to Main Menu")
            print("\n" + "=" * 60)
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.add_product()
            elif choice == '2':
                self.view_products()
            elif choice == '3':
                self.search_products()
            elif choice == '4':
                self.update_product()
            elif choice == '5':
                self.check_low_stock()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
    
    def add_product(self):
        """Add a new product."""
        self.clear_screen()
        self.display_header("ADD NEW PRODUCT")
        
        product_id = input("Product ID: ").strip()
        if product_id in self.inventory.products:
            print("Product ID already exists!")
            input("\nPress Enter to continue...")
            return
        
        name = input("Product Name: ").strip()
        try:
            price = float(input("Price: $"))
            stock = int(input("Initial Stock: "))
        except ValueError:
            print("Invalid price or stock value!")
            input("\nPress Enter to continue...")
            return
        
        category = input("Category (optional): ").strip()
        description = input("Description (optional): ").strip()
        
        product = Product(product_id, name, price, stock, category, description)
        if self.inventory.add_product(product):
            print(f"\nProduct '{name}' added successfully!")
        else:
            print("Failed to add product!")
        
        input("\nPress Enter to continue...")
    
    def view_products(self):
        """View all products."""
        self.clear_screen()
        self.display_header("ALL PRODUCTS")
        
        if not self.inventory.products:
            print("No products found!")
        else:
            print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Stock':<10}")
            print("-" * 60)
            for product in self.inventory.products.values():
                print(f"{product.product_id:<10} {product.name[:19]:<20} "
                      f"${product.price:<9.2f} {product.stock:<10}")
        
        input("\nPress Enter to continue...")
    
    def search_products(self):
        """Search products."""
        self.clear_screen()
        self.display_header("SEARCH PRODUCTS")
        
        query = input("Enter search term: ").strip()
        results = self.inventory.search_products(query)
        
        if not results:
            print("No products found!")
        else:
            print(f"\nFound {len(results)} product(s):")
            print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Stock':<10}")
            print("-" * 60)
            for product in results:
                print(f"{product.product_id:<10} {product.name[:19]:<20} "
                      f"${product.price:<9.2f} {product.stock:<10}")
        
        input("\nPress Enter to continue...")
    
    def update_product(self):
        """Update product information."""
        self.clear_screen()
        self.display_header("UPDATE PRODUCT")
        
        product_id = input("Enter Product ID: ").strip()
        product = self.inventory.get_product(product_id)
        
        if not product:
            print("Product not found!")
            input("\nPress Enter to continue...")
            return
        
        print(f"\nCurrent Product Details:")
        print(f"Name: {product.name}")
        print(f"Price: ${product.price}")
        print(f"Stock: {product.stock}")
        print(f"Category: {product.category}")
        print(f"Description: {product.description}")
        
        print("\nEnter new values (leave blank to keep current):")
        
        name = input(f"Name [{product.name}]: ").strip()
        price_str = input(f"Price [${product.price}]: ").strip()
        stock_str = input(f"Stock [{product.stock}]: ").strip()
        category = input(f"Category [{product.category}]: ").strip()
        description = input(f"Description [{product.description}]: ").strip()
        
        updates = {}
        if name:
            updates['name'] = name
        if price_str:
            try:
                updates['price'] = float(price_str)
            except ValueError:
                print("Invalid price!")
                input("\nPress Enter to continue...")
                return
        if stock_str:
            try:
                updates['stock'] = int(stock_str)
            except ValueError:
                print("Invalid stock value!")
                input("\nPress Enter to continue...")
                return
        if category:
            updates['category'] = category
        if description:
            updates['description'] = description
        
        if updates and self.inventory.update_product(product_id, **updates):
            print("Product updated successfully!")
        else:
            print("No changes made or update failed!")
        
        input("\nPress Enter to continue...")
    
    def check_low_stock(self):
        """Check for low stock products."""
        self.clear_screen()
        self.display_header("LOW STOCK ALERT")
        
        threshold = input("Enter stock threshold (default 10): ").strip()
        if not threshold:
            threshold = 10
        else:
            try:
                threshold = int(threshold)
            except ValueError:
                threshold = 10
        
        low_stock = self.inventory.get_low_stock_products(threshold)
        
        if not low_stock:
            print(f"No products with stock <= {threshold}")
        else:
            print(f"\nProducts with stock <= {threshold}:")
            print(f"{'ID':<10} {'Name':<20} {'Stock':<10}")
            print("-" * 40)
            for product in low_stock:
                print(f"{product.product_id:<10} {product.name[:19]:<20} {product.stock:<10}")
        
        input("\nPress Enter to continue...")
    
    def sales_menu(self):
        """Sales management submenu."""
        while True:
            self.clear_screen()
            self.display_header("SALES MANAGEMENT")
            print("\n1. New Sale")
            print("2. View Recent Sales")
            print("3. Back to Main Menu")
            print("\n" + "=" * 60)
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.new_sale()
            elif choice == '2':
                self.view_sales()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
    
    def new_sale(self):
        """Process a new sale."""
        self.clear_screen()
        self.display_header("NEW SALE")
        
        if not self.inventory.products:
            print("No products available for sale!")
            input("\nPress Enter to continue...")
            return
        
        # Display available products
        print("Available Products:")
        print(f"{'ID':<10} {'Name':<20} {'Price':<10} {'Stock':<10}")
        print("-" * 60)
        for product in self.inventory.products.values():
            print(f"{product.product_id:<10} {product.name[:19]:<20} "
                  f"${product.price:<9.2f} {product.stock:<10}")
        
        print("\nEnter items for sale (enter 'done' when finished):")
        items = []
        
        while True:
            product_id = input("\nProduct ID: ").strip()
            if product_id.lower() == 'done':
                break
            
            if product_id not in self.inventory.products:
                print("Invalid product ID!")
                continue
            
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive!")
                    continue
                
                product = self.inventory.products[product_id]
                if product.stock < quantity:
                    print(f"Insufficient stock! Available: {product.stock}")
                    continue
                
                items.append((product_id, quantity))
                print(f"Added: {product.name} x{quantity}")
                
            except ValueError:
                print("Invalid quantity!")
        
        if not items:
            print("No items added to sale!")
            input("\nPress Enter to continue...")
            return
        
        customer_name = input("\nCustomer Name (optional): ").strip()
        payment_method = input("Payment Method (cash/card): ").strip().lower()
        if payment_method not in ['cash', 'card']:
            payment_method = 'cash'
        
        sale = self.inventory.process_sale(items, customer_name, payment_method)
        if sale:
            print(f"\nSale processed successfully!")
            print(f"Sale ID: {sale.sale_id}")
            print(f"Total Amount: ${sale.final_amount:.2f}")
            
            # Generate receipt
            receipt = Receipt(f"REC-{sale.sale_id}", sale)
            print("\n" + receipt.generate_receipt_text())
            
            # Save receipt to file
            receipt_file = f"receipt_{receipt.receipt_id}.txt"
            with open(os.path.join(self.inventory.data_dir, receipt_file), 'w') as f:
                f.write(receipt.generate_receipt_text())
            print(f"\nReceipt saved to: {receipt_file}")
        else:
            print("Sale failed!")
        
        input("\nPress Enter to continue...")
    
    def view_sales(self):
        """View recent sales."""
        self.clear_screen()
        self.display_header("RECENT SALES")
        
        if not self.inventory.sales:
            print("No sales found!")
        else:
            # Show last 10 sales
            recent_sales = self.inventory.sales[-10:]
            print(f"Showing last {len(recent_sales)} sales:")
            
            for sale in reversed(recent_sales):
                print(f"\nSale ID: {sale.sale_id}")
                print(f"Date: {sale.date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Customer: {sale.customer_name or 'Walk-in'}")
                print(f"Total: ${sale.final_amount:.2f}")
                print("-" * 40)
        
        input("\nPress Enter to continue...")
    
    def reports_menu(self):
        """Reports submenu."""
        while True:
            self.clear_screen()
            self.display_header("REPORTS")
            print("\n1. Sales Report")
            print("2. Stock Report")
            print("3. Product Performance")
            print("4. Back to Main Menu")
            print("\n" + "=" * 60)
            
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.sales_report()
            elif choice == '2':
                self.stock_report()
            elif choice == '3':
                self.product_performance()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
    
    def sales_report(self):
        """Generate sales report."""
        self.clear_screen()
        self.display_header("SALES REPORT")
        
        print("Enter date range (leave blank for all time):")
        start_str = input("Start date (YYYY-MM-DD): ").strip()
        end_str = input("End date (YYYY-MM-DD): ").strip()
        
        start_date = None
        end_date = None
        
        if start_str:
            try:
                start_date = datetime.strptime(start_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid start date format!")
                input("\nPress Enter to continue...")
                return
        
        if end_str:
            try:
                end_date = datetime.strptime(end_str, '%Y-%m-%d')
                end_date = end_date.replace(hour=23, minute=59, second=59)
            except ValueError:
                print("Invalid end date format!")
                input("\nPress Enter to continue...")
                return
        
        report = self.inventory.get_sales_report(start_date, end_date)
        
        print(f"\nSales Report:")
        print(f"Total Sales: {report['total_sales']}")
        print(f"Total Revenue: ${report['total_revenue']:.2f}")
        print(f"Total Items Sold: {report['total_items']}")
        
        if report['product_sales']:
            print("\nTop Products:")
            sorted_products = sorted(
                report['product_sales'].items(),
                key=lambda x: x[1]['revenue'],
                reverse=True
            )[:5]
            
            for pid, data in sorted_products:
                print(f"{data['name']}: {data['quantity']} sold, ${data['revenue']:.2f} revenue")
        
        input("\nPress Enter to continue...")
    
    def stock_report(self):
        """Generate stock report."""
        self.clear_screen()
        self.display_header("STOCK REPORT")
        
        total_products = len(self.inventory.products)
        total_stock = sum(p.stock for p in self.inventory.products.values())
        low_stock = len(self.inventory.get_low_stock_products(10))
        
        print(f"Total Products: {total_products}")
        print(f"Total Stock Items: {total_stock}")
        print(f"Low Stock Items: {low_stock}")
        
        if self.inventory.products:
            print("\nStock by Category:")
            categories = {}
            for product in self.inventory.products.values():
                cat = product.category or "Uncategorized"
                if cat not in categories:
                    categories[cat] = {'count': 0, 'stock': 0}
                categories[cat]['count'] += 1
                categories[cat]['stock'] += product.stock
            
            for category, data in categories.items():
                print(f"{category}: {data['count']} products, {data['stock']} items")
        
        input("\nPress Enter to continue...")
    
    def product_performance(self):
        """Show product performance."""
        self.clear_screen()
        self.display_header("PRODUCT PERFORMANCE")
        
        report = self.inventory.get_sales_report()
        
        if not report['product_sales']:
            print("No sales data available!")
        else:
            print("Product Performance (by revenue):")
            print("-" * 60)
            
            sorted_products = sorted(
                report['product_sales'].items(),
                key=lambda x: x[1]['revenue'],
                reverse=True
            )
            
            print(f"{'Product':<20} {'Sold':<8} {'Revenue':<12}")
            print("-" * 60)
            for pid, data in sorted_products:
                print(f"{data['name'][:19]:<20} {data['quantity']:<8} ${data['revenue']:<11.2f}")
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the CLI application."""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()
            
            if choice == '1':
                self.product_menu()
            elif choice == '2':
                self.sales_menu()
            elif choice == '3':
                print("Receipt Management - Receipts are automatically generated with sales")
                print("Check the 'data' folder for receipt files")
                input("\nPress Enter to continue...")
            elif choice == '4':
                self.reports_menu()
            elif choice == '5':
                print("Thank you for using Shop Inventory System!")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")

if __name__ == "__main__":
    cli = InventoryCLI()
    cli.run()
