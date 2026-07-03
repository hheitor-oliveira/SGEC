from product import Product

class SaleItem:
    def __init__(self,
                 id: int,
                 product: Product,
                 quantity: int,
                 unitary_value: float):
        
        self.sale_item_id = id
        self.product = product
        self.quantity = quantity
        self.unitary_value = unitary_value