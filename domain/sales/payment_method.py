class PaymentMethod:
  def __init__(self,
               id: int,
               name: str,
               active: bool
               ) -> None:
    self._id = id
    self._name = name
    self._active = active