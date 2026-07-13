# lib's import's
from decimal import Decimal

# internal import's
from domain.inventory.product import Product
from domain.enums.product_categorys import Category

class ProductService:
  """Responsável por coordenar todos os processos relacionados a produtos do sistema."""
  
  def create_product(self, 
                     name: str,
                     category: Category,
                     cost_price: Decimal,
                     sale_value: Decimal) -> Product:
    
    product = Product(name, category, cost_price, sale_value)
    return product