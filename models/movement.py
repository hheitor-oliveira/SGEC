from user import User
from movement_item import MovementItem

class Movement:
    def __init__(self,
                 id,
                 movement_item: MovementItem,
                 user_id: User,
                 movement_type,
                 date
                 ):
        self.movement_id = id
        self.movement_item = movement_item
        self.user_id = user_id
        self.type = movement_type
