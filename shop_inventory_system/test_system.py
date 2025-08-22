#!/usr/bin/env python3
"""
Test script for Shop Inventory System
Tests core functionality to ensure system works correctly.
"""

import os
import sys
import tempfile
import shutil
from datetime import datetime, timedelta

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from inventory import Inventory, Product, Sale, Receipt

def test_product_creation():
    """Test product creation and basic attributes."""
    print("Testing Product Creation...")
    
    product = Product(
        product_id="TEST001",
        name="Test Product",
        price=19.99,
        stock=100,
        category="Test",
        description="A test product"
    )
    
    assert product.product_id == "TEST001"
    assert product.name == "Test Product"
    assert product.price == 19.99
    assert product.stock == 100
    assert product.category == "Test"
    
    print("✓ Product creation test passed")

def test_inventory_operations():
    """Test inventory operations."""
    print("Testing Inventory Operations...")
    
    # Create temporary directory for testing
    temp_dir = tempfile.mkdtemp()
    
    try:
        inventory = Inventory(temp_dir)
        
        # Test adding product
        product = Product("P001", "iPhone", 999.99, 50, "Electronics")
        assert inventory.add_product(product) == True
        
        # Test duplicate product
        assert inventory.add_product(product) == False
        
        # Test product retrieval
        retrieved = inventory.get_product("P001")
        assert retrieved is not None
        assert retrieved.name == "iPhone"
        
        # Test product update
        assert inventory.update_product("P001", stock=75) == True
        assert inventory.get_product("P001").stock == 75
        
        # Test search
        results = inventory.search_products("iPhone")
        assert len(results) == 1
        
        print("✓ Inventory operations test passed")
        
    finally:
        # Clean up
        shutil.rmtree(temp_dir)

def test_sales_processing():
    """Test sales processing."""
    print("Testing Sales Processing...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        inventory = Inventory(temp_dir)
        
        # Add test products
        products = [
            Product("P001", "Product A", 10.00, 100),
            Product("P002", "Product B", 20.00, 50)
        ]
        
        for product in products:
            inventory.add_product(product)
        
        # Test valid sale
        items = [("P001", 5), ("P002", 3)]
        sale = inventory.process_sale(items, "Test Customer", "cash")
        
        assert sale is not None
        assert sale.sale_id.startswith("SALE-")
        assert len(sale.items) == 2
        assert sale.total_amount == (5 * 10.00 + 3 * 20.00)
        
        # Test stock update
        assert inventory.get_product("P001").stock == 95
        assert inventory.get_product("P002").stock == 47
        
        # Test invalid sale (insufficient stock)
        items_invalid = [("P001", 200)]
        sale_invalid = inventory.process_sale(items_invalid)
        assert sale_invalid is None
        
        # Test invalid product
        items_invalid_product = [("INVALID", 1)]
        sale_invalid_product = inventory.process_sale(items_invalid_product)
        assert sale_invalid_product is None
        
        print("✓ Sales processing test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_receipt_generation():
    """Test receipt generation."""
    print("Testing Receipt Generation...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        inventory = Inventory(temp_dir)
        
        # Add product and process sale
        product = Product("P001", "Test Item", 15.99, 100)
        inventory.add_product(product)
        
        sale = inventory.process_sale([("P001", 2)], "Test Customer", "card")
        assert sale is not None
        
        # Generate receipt
        receipt = Receipt("TEST-REC-001", sale)
        receipt_text = receipt.generate_receipt_text()
        
        assert "SHOP RECEIPT" in receipt_text
        assert "Test Item" in receipt_text
        assert "Test Customer" in receipt_text
        assert "card" in receipt_text
        
        # Check receipt file creation
        receipt_file = os.path.join(temp_dir, "receipt_TEST-REC-001.txt")
        with open(receipt_file, 'w') as f:
            f.write(receipt_text)
        
        assert os.path.exists(receipt_file)
        
        print("✓ Receipt generation test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_reports():
    """Test report generation."""
    print("Testing Report Generation...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        inventory = Inventory(temp_dir)
        
        # Add products
        products = [
            Product("P001", "Product A", 10.00, 100),
            Product("P002", "Product B", 20.00, 100),
            Product("P003", "Product C", 30.00, 100)
        ]
        
        for product in products:
            inventory.add_product(product)
        
        # Process some sales
        sales_data = [
            [("P001", 5), ("P002", 3)],
            [("P002", 2), ("P003", 1)],
            [("P001", 10), ("P003", 5)]
        ]
        
        for items in sales_data:
            inventory.process_sale(items, "Test Customer", "cash")
        
        # Test sales report
        report = inventory.get_sales_report()
        
        assert report['total_sales'] == 3
        assert report['total_revenue'] > 0
        assert len(report['product_sales']) == 3
        
        # Test date filtering
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=1)
        
        filtered_report = inventory.get_sales_report(start_date, end_date)
        assert filtered_report['total_sales'] == 3
        
        # Test low stock report
        inventory.update_product("P001", stock=5)
        low_stock = inventory.get_low_stock_products(10)
        
        assert len(low_stock) >= 1
        assert any(p.product_id == "P001" for p in low_stock)
        
        print("✓ Report generation test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def test_data_persistence():
    """Test data persistence."""
    print("Testing Data Persistence...")
    
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Create inventory and add data
        inventory1 = Inventory(temp_dir)
        
        product = Product("PERSIST", "Persistent Product", 99.99, 50)
        inventory1.add_product(product)
        
        sale = inventory1.process_sale([("PERSIST", 5)], "Test", "cash")
        assert sale is not None
        
        # Create new inventory instance (should load existing data)
        inventory2 = Inventory(temp_dir)
        
        assert "PERSIST" in inventory2.products
        assert inventory2.get_product("PERSIST").stock == 45
        assert len(inventory2.sales) >= 1
        
        # Check JSON files exist
        assert os.path.exists(os.path.join(temp_dir, "products.json"))
        assert os.path.exists(os.path.join(temp_dir, "sales.json"))
        
        print("✓ Data persistence test passed")
        
    finally:
        shutil.rmtree(temp_dir)

def run_all_tests():
    """Run all tests."""
    print("Running Shop Inventory System Tests...")
    print("=" * 50)
    
    try:
        test_product_creation()
        test_inventory_operations()
        test_sales_processing()
        test_receipt_generation()
        test_reports()
        test_data_persistence()
        
        print("=" * 50)
        print("🎉 All tests passed successfully!")
        print("The Shop Inventory System is working correctly.")
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
