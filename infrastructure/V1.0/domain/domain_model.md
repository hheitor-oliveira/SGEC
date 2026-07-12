# Entity's and Attributes

## Class: Sale

### **Responsibility's**

  - Adicionar itens
  - Calcular total
  - Registrar pagamentos
  - Remover itens
  - Finalizar venda
  - Aplicar desconto

---
### **Relationships**

#####  User
  - Tipo de Relacionamento: Associação
  - -> Representa o usuário responsável pela venda.

##### Sale Item
  - Tipo de Relacionamento: Composição.
  - -> Representa os itens da venda.

##### Sale Payment
  - Tipo de Relacionamento: Composição.
  - -> Representa os pagamentos da venda.

---
### **Attribute's**

  - (#) id: int
  - (#) items: list[SalePayment]
  - (#) user: SystemUser
  - (#) total_value: Decimal
  - (#) discount_type: str
  - (#) discount_value: Decimal

---
### **Rules**

  - Domain Rule Sale 01: Uma venda é iniciada quando um produto é adicionado a ela.

  - Domain Rule Sale 02: Uma venda só poderá ser finalizada se o valor total do(s) pagamento(s) foi igual ao valor total da venda.

  - Domain Rule Sale 03: O desconto em uma venda só podera ter um tipo: Porcentagem ou Valor Exato.

  - Domain Rule Sale 04: Um pagamento só pode ser adicionado se, a soma desse pagamento com os demais já existentes não for maior que o total da venda.

  - Domain Rule Sale 05: O desconto não pode gerar um total negativo.

  - Domain Rule Sale 06: O desconto percentual deve estar entre 0% e 100%.

  - Domain Rule Sale 07: O desconto em valor não pode ultrapassar o total da venda.

---
### Public Interface

  - add_item()
  - remove_item()
  - apply_discount()
  - cancel_sale()
  - finalize_sale()

------

## Class: SaleItem

### **Responsibility's**

  - Representar um item individualmente em uma venda.
  - Calcular subtotal a partir da quantidade de items.

---
### **Relationships**

##### Sale
  - Tipo de Relacionamento: Associação
  - -> Representar os itens das vendas.

##### Product
  - Tipo de Relacionamento: Composição
  - -> Referência do produto vendido.

---
### **Attribute's**

  - (#) id: int
  - (#) product: Product
  - (#) quantity: int
  - (#) unitary_value: Decimal

---
### **Rules**

- Domain Rule Sale_Item 01: Um item em uma venda deve ter a quantidade maior que 0.

- Domain Rule Sale_Item 02: O subtotal do item tem que ser estritamente calculado em base da quantidade do produto.

---
### Public Interface

- modify_quantity()

## Class: SalePayment

### **Responsibility's**

  - Representar o(s) pagamento(s) dentro de uma venda.

---
### **Relationships**

##### Sale
  - Tipo de Relacionamento: Associação
  - -> Representa o pagamento realizado em uma venda.

##### Payment_Method
  - Tipo de Relacionamento: Composição
  - -> Representa os métodos de pagamento do sistema.

---
### **Attribute's**

  - (#) id: int
  - (#) payment_method: PaymentMethod
  - (#) payment_value: Decimal

---
### **Rules**

  - Domain Rule Payment_Method 01 - O valor do pagamento deve ser maior que 0.

---
### Public Interface

  - delete_payment()


## Class: PaymentMethod


### **Responsibility's**

  - Representar os métodos de pagamento em um pagamento.

---
### **Relationships**

##### Sale_Payment
  - Tipo de Relacionamento: Associação
  - -> Representa o método de pagamento utilizado em um pagamento.

---
### **Attribute's**

  - (#) id: int
  - (#) method: Method (enum) -> PIX, DEBIT, CREDIT
  - (#) active: bool

---
### **Rules**

  - Domain Rules PaymentMethod 01: Um método de pagamento só pode ser usado em um pagamento se ele estiver ativo.

---
### Public Interface

  - Em desenvolvimento

## Class: Product

### **Responsibility's**

  - Representar os produtos do sistema.
  - Fazer validações de entradas e saídas.
  - Controlar e representar estoque.

---
### **Relationships**

##### SaleItem
  - Tipo de Relacionamento: Associação
  - -> Representa o produto dentro de um item da venda.

##### MovementItem
  - Tipo de Relacionamento: Associação
  - -> Representa o produto dentro de uma um item da movimentação.

---
### **Attribute's**

  - (+) id: int
  - (+) name: str
  - (+) category: str
  - (#) stock_quantity: int
  - (#) sale_value: Decimal
  - (#) cost_price: Decimal
  - (+) product_Status: Status (enum) -> Active, Inactive, Descontinued

---
### **Rules**

  - Domain Rule Product 01: A quantidade em estoque de um produto não pode ser negativa.

  - Domain Rule Product 02: O produto só poderá receber uma movimentação de saída, se a quantidade de saída não for maior que sua quantidade em estoque.

  - Domain Rule Product 03: Um produto que estiver inativo não pode receber saídas através de vendas.

  - Domain Rule Product 04: Um produto que estiver descontinuado pode ser vendido, entretanto não deverá ser apontado no relatório de lista de compras.

---
### Public Interface

- remove_stock()
- add_stock()
- edit_name()
- edit_category()
- edit_status()

## Class: Movement

### **Responsibility**

  - Representar as movimentações realizadas no sistema.

---
### **Relationships**

##### Sale
- Tipo de Relacionamento: Composição
- -> Representa um dos métodos de movimentação, saídas através de vendas.

---
### **Attribute's**

- (#) id: int
- (#) items: list[MovementItem]
- (#) user: SystemUser
- (#) movement_type: MovementType (enum) -> ENTRY, EXIT
- (#) movement_date: datetime 

---
### **Rules**

- Em desenvolvimento

---
### Public Interface

- Em desenvolvimento

## Class: MovementItem

### **Responsibility's**

- R1: Representar os itens dentro de uma movimentação no sistema, permitindo assim uma movimentação com múltiplos itens.

---
### **Relationships**

##### Movement
- Tipo de Relacionamento: Composição
- -> Movimentação onde os items estão incluídos.

---
### **Attribute's**



---
### **Rules**

- Em desenvolvimento.

---
### Public Interface

- Em desenvolvimento

## Class: SystemUser

### **Responsibility's**

- R1: Representar os usuários que utilizam os sistemas, definir permissões e hierarquia.

---
### **Relationships**

##### Sale
- Tipo de Relacionamento: Composição
- -> Representa o usuário responsável pela venda.

##### Movement
- Tipo de Relacionamento: Composição
- -> Representa o usuário responsável pela movimentação.

---
### **Attribute's**


---
### **Rules**

- Em desenvolvimento.

---
### Public Interface

- Em desenvolvimento