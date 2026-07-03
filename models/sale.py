from user import User
from sale_item import SaleItem
from payment_item import PaymentItem

class Sale:
    def __init__(self,
                 id: int,
                 sale_item: SaleItem,
                 payment_item: PaymentItem,
                 user_id: User,
                 total_value: float,
                 discount: int,
                 date):
        self.sell_id = id
        self.sale_item = sale_item
        self.payment_methods = payment_item
        self.user_id = user_id
        self.total_value = total_value
        self.discount = discount
        self.date = date