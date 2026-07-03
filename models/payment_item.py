class PaymentItem:
    def __init__(self,
                 id: int,
                 payment_method: str,
                 value: float):
        self.payment_id = id
        self.payment_method = payment_method
        self.value = value