#!/usr/bin/env python3
"""
Invoice Manager for handling invoice storage and retrieval
"""

import json
import os
from datetime import datetime
from invoice import Invoice

class InvoiceManager:
    """Manages invoice storage, retrieval, and search operations"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.invoices_file = os.path.join(data_dir, "invoices.json")
        self.ensure_data_file()
    
    def ensure_data_file(self):
        """Ensure the invoices data file exists"""
        os.makedirs(self.data_dir, exist_ok=True)
        if not os.path.exists(self.invoices_file):
            with open(self.invoices_file, 'w') as f:
                json.dump([], f)
    
    def generate_invoice_number(self):
        """Generate a unique invoice number"""
        invoices = self.get_all_invoices()
        if not invoices:
            return "INV001"
        
        # Find the highest invoice number
        max_num = 0
        for inv in invoices:
            num_str = inv['invoice_number'].replace('INV', '')
            try:
                num = int(num_str)
                max_num = max(max_num, num)
            except ValueError:
                continue
        
        return f"INV{max_num + 1:03d}"
    
    def save_invoice(self, invoice):
        """Save an invoice to the data file"""
        invoice.invoice_number = self.generate_invoice_number()
        
        # Load existing invoices
        with open(self.invoices_file, 'r') as f:
            invoices = json.load(f)
        
        # Add new invoice
        invoices.append(invoice.to_dict())
        
        # Save back to file
        with open(self.invoices_file, 'w') as f:
            json.dump(invoices, f, indent=2)
        
        return invoice.invoice_number
    
    def get_all_invoices(self):
        """Get all saved invoices"""
        try:
            with open(self.invoices_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def get_invoice(self, invoice_number):
        """Get a specific invoice by number"""
        invoices = self.get_all_invoices()
        for inv in invoices:
            if inv['invoice_number'] == invoice_number:
                return inv
        return None
    
    def search_invoices(self, search_term):
        """Search invoices by number or customer details"""
        invoices = self.get_all_invoices()
        results = []
        
        search_term = search_term.lower()
        
        for inv in invoices:
            if (search_term in inv['invoice_number'].lower() or
                search_term in inv['customer_name'].lower() or
                search_term in inv['customer_email'].lower() or
                search_term in inv['customer_address'].lower()):
                results.append(inv)
        
        return results
    
    def delete_invoice(self, invoice_number):
        """Delete an invoice by number"""
        invoices = self.get_all_invoices()
        updated_invoices = [inv for inv in invoices if inv['invoice_number'] != invoice_number]
        
        if len(updated_invoices) == len(invoices):
            return False  # Invoice not found
        
        with open(self.invoices_file, 'w') as f:
            json.dump(updated_invoices, f, indent=2)
        
        return True
    
    def get_invoice_stats(self):
        """Get statistics about all invoices"""
        invoices = self.get_all_invoices()
        
        if not invoices:
            return {
                'total_invoices': 0,
                'total_revenue': 0.0,
                'average_invoice_value': 0.0,
                'most_recent_invoice': None
            }
        
        total_revenue = sum(inv['total'] for inv in invoices)
        average_value = total_revenue / len(invoices)
        
        # Sort by date to get most recent
        sorted_invoices = sorted(invoices, key=lambda x: x['date'], reverse=True)
        most_recent = sorted_invoices[0] if sorted_invoices else None
        
        return {
            'total_invoices': len(invoices),
            'total_revenue': total_revenue,
            'average_invoice_value': average_value,
            'most_recent_invoice': most_recent
        }
    
    def backup_invoices(self, backup_filename=None):
        """Create a backup of all invoices"""
        if backup_filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"invoices_backup_{timestamp}.json"
        
        backup_path = os.path.join(self.data_dir, backup_filename)
        
        invoices = self.get_all_invoices()
        with open(backup_path, 'w') as f:
            json.dump(invoices, f, indent=2)
        
        return backup_path
    
    def restore_from_backup(self, backup_filename):
        """Restore invoices from a backup file"""
        backup_path = os.path.join(self.data_dir, backup_filename)
        
        if not os.path.exists(backup_path):
            return False
        
        try:
            with open(backup_path, 'r') as f:
                invoices = json.load(f)
            
            with open(self.invoices_file, 'w') as f:
                json.dump(invoices, f, indent=2)
            
            return True
        except (json.JSONDecodeError, IOError):
            return False
