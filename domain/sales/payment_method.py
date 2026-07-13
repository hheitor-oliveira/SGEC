from domain.enums.payment_methods import Method

class PaymentMethod:
  def __init__(self,
               id: int,
               method: Method,
               active: bool
               ) -> None:
    self._id = id
    self._method = method
    self._active = active