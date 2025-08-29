# Shop Inventory System

A comprehensive Python-based inventory management system designed to track stock, sales, and receipts for retail businesses.

## Features

### ✅ Core Functionality

- **Product Management**: Add, update, and delete products with detailed information
- **Stock Tracking**: Real-time inventory levels with low-stock alerts
- **Sales Processing**: Complete sales transactions with automatic stock updates
- **Receipt Generation**: Automatic receipt creation for every sale
- **Reporting**: Comprehensive sales and stock reports

### ✅ Advanced Features
- **Search & Filter**: Search products by name, category, or ID
- **Date Range Reports**: Filter sales reports by custom date ranges
- **Product Performance**: Track best-selling products by revenue
- **Low Stock Alerts**: Identify products needing restocking
- **Data Persistence**: All data saved to JSON files for reliability

## Quick Start

### Installation
1. Clone or download the project
2. Navigate to the `shop_inventory_system` directory
3. No additional dependencies required - uses Python standard library

### Running the System
```bash
# Navigate to the project directory
cd shop_inventory_system

# Run the CLI application
python main.py
```

## Usage Guide

### Getting Started
1. **Launch the system**: Run `python main.py`
2. **Add products**: Use Product Management → Add New Product
3. **Process sales**: Use Sales Management → New Sale
4. **Generate reports**: Use Reports → Sales Report

### Menu Navigation
The system uses a hierarchical menu structure:
- **Main Menu**: Primary navigation
- **Product Management**: Handle all product operations
- **Sales Management**: Process sales and view history
- **Reports**: Generate various business reports

## Detailed Usage

### Product Management
```python
# Add a new product
Product ID: P001
Name: iPhone 14
Price: 999.99
Stock: 50
Category: Electronics
Description: Latest Apple smartphone
```

### Sales Processing
```python
# Process a new sale
Customer: John Doe
Items:
- iPhone 14 (P001) x2
- AirPods (P002) x1
Payment: Cash
```

### Reports
- **Sales Report**: Total revenue, items sold, date filtering
- **Stock Report**: Current inventory levels, low stock alerts
- **Product Performance**: Best-selling products by revenue

## Data Storage

All data is automatically saved to JSON files in the `data/` directory:
- `products.json`: Product catalog
- `sales.json`: Transaction history
- `receipts.json`: Receipt records

## File Structure

```
shop_inventory_system/
├── inventory.py      # Core inventory classes
├── main.py          # CLI interface
├── requirements.txt  # Dependencies
├── README.md        # Documentation
└── data/            # Data storage directory
    ├── products.json
    ├── sales.json
    └── receipts.json
```

## API Reference

### Core Classes

#### Product
Represents individual products with attributes:
- `product_id`: Unique identifier
- `name`: Product name
- `price`: Unit price
- `stock`: Current stock level
- `category`: Product category
- `description`: Product description

#### Sale
Represents completed sales with:
- `sale_id`: Unique transaction ID
- `items`: List of sold items
- `customer_name`: Customer information
- `payment_method`: Payment type
- `total_amount`: Final sale amount

#### Receipt
Automatically generated for each sale with:
- `receipt_id`: Unique receipt identifier
- `sale`: Associated sale transaction
- `formatted_text`: Printable receipt format

### Key Methods

#### Inventory Class
- `add_product(product)`: Add new product
- `process_sale(items, customer, payment)`: Process sale
- `get_sales_report(start_date, end_date)`: Generate sales report
- `search_products(query)`: Search products
- `get_low_stock_products(threshold)`: Find low stock items

## Examples

### Adding Products
```python
# Through CLI
1. Select Product Management → Add New Product
2. Enter product details
3. Product added to inventory

# Programmatically
product = Product("P001", "iPhone 14", 999.99, 50, "Electronics", "Latest model")
inventory.add_product(product)
```

### Processing Sales
```python
# Through CLI
1. Select Sales Management → New Sale
2. Choose products and quantities
3. Enter customer details
4. Complete transaction

# Programmatically
items = [("P001", 2), ("P002", 1)]
sale = inventory.process_sale(items, "John Doe", "cash")
```

### Generating Reports
```python
# Through CLI
1. Select Reports → Sales Report
2. Choose date range
3. View detailed report

# Programmatically
report = inventory.get_sales_report(
    start_date=datetime(2024, 1, 1),
    end_date=datetime(2024, 12, 31)
)
```

## Troubleshooting

### Common Issues

1. **"Product not found"**
   - Verify product ID exists in inventory
   - Check spelling and case sensitivity

2. **"Insufficient stock"**
   - Check current stock levels
   - Update stock before processing sale

3. **"Invalid date format"**
   - Use YYYY-MM-DD format for dates
   - Example: 2024-03-15

### Data Recovery
All data is stored in JSON format. If needed:
- Backup `data/` directory regularly
- JSON files can be edited manually if necessary
- System automatically loads data on startup

## Contributing

Feel free to enhance the system by:
- Adding web interface (Flask/Django)
- Implementing barcode scanning
- Adding supplier management
- Creating email notifications
- Adding export functionality (CSV/Excel)

## License

This project is open source and available under the MIT License.
