# lib's imports
from decimal import Decimal

# internal imports
from domain.inventory.product import Product

class SaleItem:
    """
    
    """
    def __init__(self,
                 id: int,
                 product: Product,
                 quantity: int,
                 unitary_value: Decimal):
        
        self._id = id
        self._product = product
        self._quantity = quantity
        self._unitary_value = unitary_value