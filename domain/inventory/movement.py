# lib's imports
from datetime import datetime

# internal imports
from domain.users.system_user import SystemUser
from domain.inventory.movement_item import MovementItem


class Movement:
    """
    
    """
    def __init__(self,
                 id: int,
                 items: list[MovementItem],
                 user: SystemUser,
                 type: int,
                 date: datetime
                 ):
        self.movement_id = id
        self.items = items
        self.user = user
        self.type = type
        self.date = date
