# Casos de uso

### Venda

### Caso de Uso -> Venda - Cadastrar produto
  - Objetivo: Cadastrar um novo produto no sistema.

  - #### Fluxo
    1 - Usuário interage na interface.
    2 - É aberto a interface de cadastro de produto.
    3 - Usuário preenche as informações necessárias.
    4 - SaleService cria o objeto Produto em memória.
    5 - SaleService solicita uma conexão ao banco de dados.
    6 - SaleService solicita o "save" ao SaleRepository.
    7 - SaleRepository persiste o produto no banco.
---
