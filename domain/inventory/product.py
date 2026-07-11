class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 category: str,
                 stock_quantity: int,
                 sale_value: float,
                 cost_price: float,
                 status: str
                 ):
        self.id = id
        self.name = name
        self.category = category
        self.stock_quantity = stock_quantity
        self.sale_value = sale_value
        self.cost_price = cost_price
        self.status = status
