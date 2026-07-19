class Category:
  def __init__(self,
               category_name: str,
               id: None | int = None):
    self._id = id
    self._category_name = category_name
    
  @property
  def category_name(self) -> str:
    return self._category_name