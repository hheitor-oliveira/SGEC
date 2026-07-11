# lib's imports
from datetime import datetime

# internals imports
from domain.users.system_user import SystemUser
from domain.sales.sale_item import SaleItem
from domain.sales.sale_payment import SalePayment

class Sale:
    """
    
    """
    def __init__(self,
                 id: int,
                 items: list[SaleItem],
                 sale_payment: list[SalePayment],
                 user: SystemUser,
                 total_value: float,
                 discount: int,
                 sale_date: datetime):

        self.id = id
        self.items = items
        self.sale_payment = sale_payment
        self.user = user
        self.total_value = total_value
        self.discount = discount
        self.sale_date = sale_date
        