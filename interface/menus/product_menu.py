# lib's import's

# internal import's
from interface.terminal import Terminal
from domain.enums.product_categorys import Category
from services.inventory.product_service import ProductService

class ProductMenu:
  
  def __init__(self):
    self._product_service = ProductService()
  
  def run(self):
    '''Interface principal dos produtos.'''
    while True:
      Terminal.header('Menu Produtos - SGEC')
      
      print('1 - Cadastros')
      print('2 - Alterações')
      print('3 - Movimentações')
      print('4 - Sair')
      
      Terminal.separator()
      
      user_choice = Terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        self.create_product_screen()
      elif user_choice == 2:
        input()
        Terminal.clear()
        break
      elif user_choice == 3:
        input()
        Terminal.clear()
        break
      elif user_choice == 4:
        input()
        Terminal.clear()
        break
      elif user_choice == 5:
        input()
        Terminal.clear()
        break
      elif user_choice == 6:
        break
  
  def select_product_screen(self) -> None:
    pass
  
  def create_product_screen(self) -> None:
    '''Interface de criação de um produto no terminal.'''
    name = None
    selected_category = None
    cost_price = None
    sale_value = None
    
    while True:
      Terminal.clear()

      Terminal.header('Cadastro de Produto - SGEC')
      
      print('1 - Nome:', name) if name else print('1 - Nome: Não informado')
      print('2 - Categoria:', selected_category.value) if selected_category else print('2 - Categoria: Não selecionado')
      print('3 - Preço de custo:', cost_price) if cost_price else print('3 - Preço de custo: Não informado')
      print('4 - Valor de venda:', sale_value) if sale_value else print('4 - Valor de venda: Não informado')
      Terminal.separator()
      print('5 - Finalizar cadastro')

      Terminal.separator()

      option = Terminal.ask_int('Escolha um campo: ')

      if option == 1:
        name = Terminal.ask('Nome')

      elif option == 2:
        for index, item in enumerate(Category, start=1):
          print(f'{index} - {item.value}')
          
        option = Terminal.ask_int('Seleciona uma das categorias acima')  
        categories_list = list(Category)
        selected_category = categories_list[option - 1]
        
      elif option == 3:
        cost_price = Terminal.ask_decimal('Preço de custo')

      elif option == 4:
        sale_value = Terminal.ask_decimal('Preço de Venda')
      
      elif option == 5:
        if name and selected_category and cost_price and sale_value != None:
          self._product_service.create_product(name, selected_category, cost_price, sale_value)
          Terminal.success('Produto cadastrado com sucesso!')
          Terminal.pause()
          break
        else:
          Terminal.error('Preencha todos os campos antes de continuar!')
          Terminal.pause()
          continue
        
  def edit_product_screen(self) -> None:
    Terminal.header('Operações de Alteração de Produtos - SGEC')
    print('1 - Alterar nome do produto')
    print('2 - Alterar categoria do produto')
    print('3 - Alterar preço de custo do produto.')
    print('4 - Alterar valor de venda do produto.')
    print('5 - Alterar status do produto.')
    print('6 - Sair')
    Terminal.separator
    Terminal.ask_int('Escolha a alteração para ser realizada.')
   
  def movement_product_screen(self) -> None:
    while True:
      Terminal.header('Movimentações de Produto - SGEC')
      print('1 - Dar entrada em um produto.')
      print('2 - Dar saída em um produto.')
      print('3 - Sair')
      Terminal.separator()
      option = Terminal.ask_int('Escolha a operação desejada.')
      
      if option == 1:
        pass
      if option == 2:
        pass
      if option == 3:
        break