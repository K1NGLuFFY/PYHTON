# Invoice Generator - Python

A comprehensive invoice generation system built with Python that allows you to create, manage, and export professional invoices.

## Features

- **Create Professional Invoices**: Generate invoices with customer details and itemized billing
- **PDF Export**: Automatically generate PDF invoices with professional formatting
- **Invoice Management**: Save, search, and manage all your invoices in one place
- **Tax Calculations**: Automatic tax calculations with customizable tax rates
- **Backup & Restore**: Built-in backup and restore functionality
- **Statistics**: View revenue and invoice statistics
- **User-Friendly Interface**: Simple command-line interface for easy operation

## Installation

1. Clone or download this project
2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
python main.py
```

### Creating an Invoice

1. Select "Create New Invoice" from the main menu
2. Enter customer details (name, email, address)
3. Add items with descriptions, quantities, and prices
4. Set tax rate (as percentage)
5. Save the invoice

### Exporting to PDF

1. After creating an invoice, choose to generate PDF
2. Or use option 4 from main menu to export existing invoices
3. PDFs are saved in the `invoices/` directory

## File Structure

```
invoice_generator/
├── main.py              # Main application entry point
├── invoice.py           # Invoice class definition
├── invoice_manager.py   # Invoice storage and management
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── data/              # Invoice data storage
├── invoices/          # Generated PDF invoices
└── README.md         # This file
```

## Example Usage

```python
from invoice import Invoice

# Create a new invoice
invoice = Invoice("John Doe", "john@example.com", "123 Main St")

# Add items
invoice.add_item("Web Development", 10, 100.00)
invoice.add_item("Domain Registration", 1, 15.00)

# Set tax rate
invoice.set_tax_rate(18.5)

# Generate PDF
invoice.generate_pdf("my_invoice.pdf")
```

## Configuration

- **Data Storage**: Invoices are stored in JSON format in `data/invoices.json`
- **PDF Location**: Generated PDFs are saved in `invoices/` directory
- **Backup**: Automatic backups created in `backups/` directory

## Troubleshooting

### Common Issues

1. **Permission Errors**: Ensure you have write permissions in the application directory
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **PDF Generation Issues**: Check that `invoices/` directory exists

### Support

For issues or questions, please check the documentation or create an issue in the project repository.

## License

This project is open source and available under the MIT License.
