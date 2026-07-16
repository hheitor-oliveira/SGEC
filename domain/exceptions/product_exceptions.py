class ProductError(Exception):
  '''Classe base para exceções relacionadas a produtos.'''
  pass

class InvalidStockQuantityError(ProductError):
  '''A quantidade para entrada deve ser maior que 0.'''
  pass