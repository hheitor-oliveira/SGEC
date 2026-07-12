# lib's imports
from decimal import Decimal

# internal import's
from domain.enums.product_status import ProductStatus

class Product:
    def __init__(self,
                 id: int,
                 name: str,
                 category: str,
                 stock_quantity: int,
                 sale_value: Decimal,
                 cost_price: Decimal,
                 product_status: ProductStatus
                 ):
        self._id = id
        self.name = name
        self.category = category
        self._stock_quantity = stock_quantity
        self._sale_value = sale_value
        self._cost_price = cost_price
        self.status = product_status
