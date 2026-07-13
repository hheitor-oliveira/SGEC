# lib's import's

# internal import's
from interface.terminal import terminal
from domain.enums.product_categorys import Category

class ProductMenu:
  
  def run(self):
    
    while True:
      terminal.header('Menu Produtos - SGEC')
      
      print('1 - Cadastrar Produto')
      print('2 - Remover Produto')
      print('3 - Editar Produto')
      print('4 - Dar entrada em Produto')
      print('5 - Dar saída em Produto')
      print('6 - Sair')
      
      terminal.separator()
      
      user_choice = terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        self.show_create_product_screen()
      elif user_choice == 2:
        input()
        terminal.clear()
        break
      elif user_choice == 3:
        input()
        terminal.clear()
        break
      elif user_choice == 4:
        input()
        terminal.clear()
        break
      elif user_choice == 5:
        input()
        terminal.clear()
        break
      elif user_choice == 6:
        break
  
  def show_create_product_screen(self):
    
    name = None
    category = None
    cost_price = None
    sale_price = None
    
    while True:
      terminal.clear()

      terminal.header('Cadastro de Produto - SGEC')
      
      print("1 - Nome:", name)
      print("2 - Categoria:", category)
      print("3 - Preço de custo:", cost_price)
      print("4 - Preço de venda:", sale_price)

      terminal.separator()

      option = input("Escolha um campo: ")

      if option == "1":
        name = input("Nome: ")

      elif option == "2":
        for index, category in enumerate(Category, start=1):
          print(f"{index} - {category.value}")
        option = terminal.ask_int('Categoria: ')
        categories = list(Category)
        category = categories[option - 1].value

      elif option == "3":
        cost_price = terminal.ask_decimal('Preço de custo')

      elif option == "4":
        sale_price = terminal.ask_decimal('Preço de Venda')
        
product_menu = ProductMenu()