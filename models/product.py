class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 category: str,
                 quantity: int,
                 value: float,
                 buy_price: float
                 ):
        self.product_id = id
        self.product_name = name
        self.product_category = category
        self.product_quantity = quantity
        self.product_value = value
        self.buy_price = buy_price
        
