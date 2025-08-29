#!/usr/bin/env python3
"""
Shop Inventory System - Quick Demo
A simple demonstration of the system capabilities.
"""

import os
import sys

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from inventory import Inventory, Product

def main():
    print("🛍️ Shop Inventory System - Quick Demo")
    print("=" * 50)
    
    # Create demo inventory
    inventory = Inventory()
    
    # Add demo products
    print("\n📦 Adding demo products...")
    
    products = [
        Product("IPHONE14", "iPhone 14", 999.99, 50, "Electronics", "Latest Apple smartphone"),
        Product("AIRPODS", "AirPods Pro", 249.99, 100, "Electronics", "Wireless earbuds"),
        Product("MACBOOK", "MacBook Air", 1299.99, 25, "Electronics", "Apple laptop"),
        Product("IPAD", "iPad Pro", 799.99, 75, "Electronics", "Apple tablet"),
        Product("APPLEWATCH", "Apple Watch", 399.99, 150, "Electronics", "Smart watch")
    ]
    
    for product in products:
        inventory.add_product(product)
    
    print(f"✅ Added {len(products)} demo products")
    
    # Display products
    print("\n📋 Available Products:")
    print(f"{'ID':<12} {'Name':<15} {'Price':<10} {'Stock':<8}")
    print("-" * 45)
    for product in inventory.products.values():
        print(f"{product.product_id:<12} {product.name[:14]:<15} ${product.price:<9.2f} {product.stock:<8}")
    
    # Show low stock alert
    low_stock = inventory.get_low_stock_products(30)
    if low_stock:
        print(f"\n⚠️ Low Stock Alert ({len(low_stock)} products):")
        for product in low_stock:
            print(f"  {product.name}: {product.stock} remaining")
    
    print("\n🎯 System is ready to use!")
    print("\nTo start using the system:")
    print("1. Run: python main.py")
    print("2. Select Product Management → Add New Product")
    print("3. Select Sales Management → New Sale")
    print("4. Select Reports → Sales Report")

if __name__ == "__main__":
    main()
