# lib's imports
from decimal import Decimal

# internal imports
from domain.sales.payment_method import PaymentMethod


class SalePayment:
    '''Classe responsável por representar um pagamento individualmente realizado em uma venda. (Sale <- SalePayment)'''
    def __init__(self,
                 id: int,
                 payment_method: PaymentMethod,
                 payment_value: Decimal):
        
        self._id = id
        self._payment_method = payment_method
        self._payment_value = payment_value