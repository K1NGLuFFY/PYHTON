#!/usr/bin/env python3
"""
Invoice class for managing individual invoices
"""

from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import os

class Invoice:
    """Represents a single invoice with customer details and items"""
    
    def __init__(self, customer_name, customer_email, customer_address):
        self.invoice_number = None
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_address = customer_address
        self.items = []
        self.tax_rate = 0.0
    
    def add_item(self, description, quantity, unit_price):
        """Add an item to the invoice"""
        self.items.append({
            'description': description,
            'quantity': quantity,
            'unit_price': unit_price
        })
    
    def set_tax_rate(self, tax_rate):
        """Set the tax rate as a percentage"""
        self.tax_rate = tax_rate
    
    def calculate_subtotal(self):
        """Calculate the subtotal before tax"""
        return sum(item['quantity'] * item['unit_price'] for item in self.items)
    
    def calculate_tax(self):
        """Calculate the tax amount"""
        return self.calculate_subtotal() * (self.tax_rate / 100)
    
    def calculate_total(self):
        """Calculate the total amount including tax"""
        return self.calculate_subtotal() + self.calculate_tax()
    
    def to_dict(self):
        """Convert invoice to dictionary for JSON serialization"""
        return {
            'invoice_number': self.invoice_number,
            'date': self.date,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'customer_address': self.customer_address,
            'items': self.items,
            'tax_rate': self.tax_rate,
            'subtotal': self.calculate_subtotal(),
            'tax_amount': self.calculate_tax(),
            'total': self.calculate_total()
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create Invoice instance from dictionary"""
        invoice = cls(
            data['customer_name'],
            data['customer_email'],
            data['customer_address']
        )
        invoice.invoice_number = data['invoice_number']
        invoice.date = data['date']
        invoice.items = data['items']
        invoice.tax_rate = data['tax_rate']
        return invoice
    
    def generate_pdf(self, filename=None):
        """Generate a PDF version of the invoice"""
        if filename is None:
            filename = f"invoice_{self.invoice_number}.pdf"
        
        # Ensure the directory exists
        os.makedirs("invoices", exist_ok=True)
        filepath = os.path.join("invoices", filename)
        
        doc = SimpleDocTemplate(filepath, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1  # Center alignment
        )
        story.append(Paragraph("INVOICE", title_style))
        story.append(Spacer(1, 12))
        
        # Invoice details
        invoice_info = f"""
        <b>Invoice #{self.invoice_number}</b><br/>
        <b>Date:</b> {self.date}<br/>
        """
        story.append(Paragraph(invoice_info, styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Customer details
        customer_info = f"""
        <b>BILL TO:</b><br/>
        {self.customer_name}<br/>
        {self.customer_email}<br/>
        {self.customer_address}<br/>
        """
        story.append(Paragraph(customer_info, styles['Normal']))
        story.append(Spacer(1, 30))
        
        # Items table
        if self.items:
            table_data = [['Description', 'Quantity', 'Unit Price', 'Total']]
            
            for item in self.items:
                total = item['quantity'] * item['unit_price']
                table_data.append([
                    item['description'],
                    str(item['quantity']),
                    f"${item['unit_price']:.2f}",
                    f"${total:.2f}"
                ])
            
            # Add subtotal, tax, and total rows
            subtotal = self.calculate_subtotal()
            tax = self.calculate_tax()
            total = self.calculate_total()
            
            table_data.extend([
                ['', '', '', ''],
                ['', '', 'Subtotal:', f"${subtotal:.2f}"],
                ['', '', f'Tax ({self.tax_rate}%):', f"${tax:.2f}"],
                ['', '', 'TOTAL:', f"${total:.2f}"]
            ])
            
            table = Table(table_data, colWidths=[3*inch, 1*inch, 1.5*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -4), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (-2, -3), (-1, -1), 'Helvetica-Bold'),
                ('BACKGROUND', (-2, -3), (-1, -1), colors.lightgrey),
            ]))
            
            story.append(table)
        
        doc.build(story)
        return filepath
