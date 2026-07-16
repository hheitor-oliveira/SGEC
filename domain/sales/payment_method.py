from domain.enums.payment_methods import Method

class PaymentMethod:
  '''Classe responsável por representar os métodos de pagamentos de uma venda no sistema. (Sale <- SalePayment <- PaymentMethod)'''
  def __init__(self,
               id: int,
               method: Method,
               active: bool
               ) -> None:
    self._id = id
    self._method = method
    self._active = active