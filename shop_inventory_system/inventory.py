import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class Product:
    """Represents a product in the inventory."""
    
    def __init__(self, product_id: str, name: str, price: float, stock: int, 
                 category: str = "", description: str = ""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.description = description
        self.last_updated = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert product to dictionary for JSON serialization."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'stock': self.stock,
            'category': self.category,
            'description': self.description,
            'last_updated': self.last_updated.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Product':
        """Create product from dictionary."""
        product = cls(
            data['product_id'],
            data['name'],
            data['price'],
            data['stock'],
            data.get('category', ''),
            data.get('description', '')
        )
        product.last_updated = datetime.fromisoformat(data['last_updated'])
        return product

class SaleItem:
    """Represents an item in a sale."""
    
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price
        self.total_price = self.unit_price * self.quantity

class Sale:
    """Represents a sale transaction."""
    
    def __init__(self, sale_id: str, items: List[SaleItem], 
                 customer_name: str = "", payment_method: str = "cash"):
        self.sale_id = sale_id
        self.items = items
        self.customer_name = customer_name
        self.payment_method = payment_method
        self.total_amount = sum(item.total_price for item in items)
        self.tax_amount = self.total_amount * 0.08  # 8% tax
        self.final_amount = self.total_amount + self.tax_amount
        self.date = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert sale to dictionary for JSON serialization."""
        return {
            'sale_id': self.sale_id,
            'items': [
                {
                    'product_id': item.product.product_id,
                    'product_name': item.product.name,
                    'quantity': item.quantity,
                    'unit_price': item.unit_price,
                    'total_price': item.total_price
                }
                for item in self.items
            ],
            'customer_name': self.customer_name,
            'payment_method': self.payment_method,
            'total_amount': self.total_amount,
            'tax_amount': self.tax_amount,
            'final_amount': self.final_amount,
            'date': self.date.isoformat()
        }

class Receipt:
    """Represents a purchase receipt."""
    
    def __init__(self, receipt_id: str, sale: Sale):
        self.receipt_id = receipt_id
        self.sale = sale
        self.receipt_date = datetime.now()
    
    def generate_receipt_text(self) -> str:
        """Generate formatted receipt text."""
        receipt_lines = []
        receipt_lines.append("=" * 50)
        receipt_lines.append("SHOP RECEIPT".center(50))
        receipt_lines.append("=" * 50)
        receipt_lines.append(f"Receipt ID: {self.receipt_id}")
        receipt_lines.append(f"Date: {self.receipt_date.strftime('%Y-%m-%d %H:%M:%S')}")
        receipt_lines.append(f"Customer: {self.sale.customer_name or 'Walk-in'}")
        receipt_lines.append("-" * 50)
        receipt_lines.append("Items:")
        receipt_lines.append("-" * 50)
        
        for item in self.sale.items:
            receipt_lines.append(
                f"{item.product.name[:20]:<20} x{item.quantity:<3} "
                f"${item.unit_price:>6.2f} = ${item.total_price:>7.2f}"
            )
        
        receipt_lines.append("-" * 50)
        receipt_lines.append(f"Subtotal: ${self.sale.total_amount:>35.2f}")
        receipt_lines.append(f"Tax (8%): ${self.sale.tax_amount:>35.2f}")
        receipt_lines.append(f"Total: ${self.sale.final_amount:>37.2f}")
        receipt_lines.append(f"Payment: {self.sale.payment_method.title():>34}")
        receipt_lines.append("=" * 50)
        receipt_lines.append("Thank you for shopping with us!")
        receipt_lines.append("=" * 50)
        
        return "\n".join(receipt_lines)

class Inventory:
    """Main inventory management system."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.products: Dict[str, Product] = {}
        self.sales: List[Sale] = []
        self.receipts: List[Receipt] = []
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Load existing data
        self.load_data()
    
    def add_product(self, product: Product) -> bool:
        """Add a new product to inventory."""
        if product.product_id in self.products:
            return False
        
        self.products[product.product_id] = product
        self.save_products()
        return True
    
    def update_product(self, product_id: str, **kwargs) -> bool:
        """Update product information."""
        if product_id not in self.products:
            return False
        
        product = self.products[product_id]
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
        product.last_updated = datetime.now()
        
        self.save_products()
        return True
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Get product by ID."""
        return self.products.get(product_id)
    
    def search_products(self, query: str) -> List[Product]:
        """Search products by name or category."""
        query = query.lower()
        return [
            product for product in self.products.values()
            if query in product.name.lower() or query in product.category.lower()
        ]
    
    def get_low_stock_products(self, threshold: int = 10) -> List[Product]:
        """Get products with stock below threshold."""
        return [
            product for product in self.products.values()
            if product.stock <= threshold
        ]
    
    def process_sale(self, items: List[Tuple[str, int]], 
                     customer_name: str = "", payment_method: str = "cash") -> Optional[Sale]:
        """Process a sale transaction."""
        sale_items = []
        
        # Validate stock availability
        for product_id, quantity in items:
            if product_id not in self.products:
                return None
            
            product = self.products[product_id]
            if product.stock < quantity:
                return None
        
        # Create sale items and update stock
        for product_id, quantity in items:
            product = self.products[product_id]
            product.stock -= quantity
            sale_items.append(SaleItem(product, quantity))
        
        # Create sale and receipt
        sale_id = f"SALE-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        sale = Sale(sale_id, sale_items, customer_name, payment_method)
        
        receipt_id = f"REC-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        receipt = Receipt(receipt_id, sale)
        
        # Save data
        self.sales.append(sale)
        self.receipts.append(receipt)
        self.save_sales()
        self.save_receipts()
        self.save_products()
        
        return sale
    
    def get_sales_report(self, start_date: Optional[datetime] = None,
                        end_date: Optional[datetime] = None) -> Dict:
        """Generate sales report."""
        if not start_date:
            start_date = datetime.min
        if not end_date:
            end_date = datetime.max
        
        filtered_sales = [
            sale for sale in self.sales
            if start_date <= sale.date <= end_date
        ]
        
        total_sales = len(filtered_sales)
        total_revenue = sum(sale.final_amount for sale in filtered_sales)
        total_items = sum(len(sale.items) for sale in filtered_sales)
        
        # Product sales breakdown
        product_sales = {}
        for sale in filtered_sales:
            for item in sale.items:
                key = item.product.product_id
                if key not in product_sales:
                    product_sales[key] = {
                        'name': item.product.name,
                        'quantity': 0,
                        'revenue': 0.0
                    }
                product_sales[key]['quantity'] += item.quantity
                product_sales[key]['revenue'] += item.total_price
        
        return {
            'total_sales': total_sales,
            'total_revenue': total_revenue,
            'total_items': total_items,
            'product_sales': product_sales,
            'sales': filtered_sales
        }
    
    def save_products(self):
        """Save products to JSON file."""
        products_data = {
            pid: product.to_dict() 
            for pid, product in self.products.items()
        }
        with open(os.path.join(self.data_dir, 'products.json'), 'w') as f:
            json.dump(products_data, f, indent=2)
    
    def save_sales(self):
        """Save sales to JSON file."""
        sales_data = [sale.to_dict() for sale in self.sales]
        with open(os.path.join(self.data_dir, 'sales.json'), 'w') as f:
            json.dump(sales_data, f, indent=2)
    
    def save_receipts(self):
        """Save receipts to JSON file."""
        receipts_data = [
            {
                'receipt_id': receipt.receipt_id,
                'sale': receipt.sale.to_dict(),
                'receipt_date': receipt.receipt_date.isoformat()
            }
            for receipt in self.receipts
        ]
        with open(os.path.join(self.data_dir, 'receipts.json'), 'w') as f:
            json.dump(receipts_data, f, indent=2)
    
    def load_data(self):
        """Load data from JSON files."""
        # Load products
        products_file = os.path.join(self.data_dir, 'products.json')
        if os.path.exists(products_file):
            with open(products_file, 'r') as f:
                products_data = json.load(f)
                self.products = {
                    pid: Product.from_dict(data)
                    for pid, data in products_data.items()
                }
        
        # Load sales
        sales_file = os.path.join(self.data_dir, 'sales.json')
        if os.path.exists(sales_file):
            with open(sales_file, 'r') as f:
                sales_data = json.load(f)
                # Note: This is simplified - in practice, you'd need to reconstruct
                # the full Sale objects with Product references
