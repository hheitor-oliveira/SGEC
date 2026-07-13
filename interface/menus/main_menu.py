from interface.terminal import terminal
from interface.menus.product_menu import product_menu

class MainMenu:
  
  def run(self) -> None:
    
    while True:
      
      terminal.header("Menu Principal - SGEC")
      
      print('1 - Produtos')
      print('2 - Vendas (Em desenvolvimento)')
      print('3 - Sair')
      
      terminal.separator()
      
      user_choice = terminal.ask_int('Escolha a opção desejada')
      
      if user_choice == 1:
        product_menu.run()
        
      elif user_choice == 2:
        print('Em desenvolvimento, clique qualquer tecla para continuar.')
        input()
        terminal.clear()
        continue
      
      elif user_choice == 3:
        break