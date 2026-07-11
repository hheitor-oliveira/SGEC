# Entity's and Attributes

## Class: Sale

### **Responsibility's**

- R -> Representar as vendas realizadas no sistema, tendo a função de gerir todas as classes dependentes (sale_item, sale_payment, payment_method) para registrar corretamente as vendas.

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
### **Rules**

- Domain Rule Sale 01 - Uma venda só poderá ser concluída quando o total dos pagamentos for igual ao valor total da venda.

- Domain Rule Sale 02 - Uma venda é iniciada quando um produto é adicionado a ela.

- Domain Rule Sale 03 - Os descontos serão aplicados no valor total da venda, não permitindo desconto individual entre produtos.

---
### Public Interface

- Em desenvolvimento

------
## Class: SaleItem

### **Responsibility's**

- R -> Representar os itens de uma venda, e permitir que existam vários items na mesma venda, identificando eles individualmente com nome e valores e quantidade.

---
### **Relationships**

##### Sale
- Tipo de Relacionamento: Composição
- -> Representar os itens das vendas.
- 
Product
- Tipo de Relacionamento: Associação
- -> Referência do produto vendido.

---
### **Rules**

- Domain Rule Sale_Item 01: Um item da venda tem a quantidade padrão de 1.
- Domain Rule Sale_Item 02: Um item só pode ser adicionado se a quantidade em estoque for o suficiente.

---
### Public Interface

- Em desenvolvimento


## Class: SalePayment

### **Responsibility's**

- R -> Representar os pagamentos realizados nas vendas, fazendo a validação da entrada dos pagamentos.

---
### **Relationships**

##### Sale
- Tipo de Relacionamento: Composição
- -> Representa o pagamento realizado em uma venda.

##### Payment_Method
- Tipo de Relacionamento: Composição
- -> Representa os métodos de pagamento do sistema.
---
### **Rules**

- Domain Rule Payment_Method 01 - O valor de um pagamento tem que ser maior que 0.
- Domain Rule Payment_Method 02 - Os pagamentos não podem ter o valor maior que o valor total dos produtos.

---
### Public Interface

- Em desenvolvimento


## Class: PaymentMethod

### **Responsibility's**

- R -> Representar os métodos de pagamento de uma venda.

---
### **Relationships**

##### Sale_Payment
- Tipo de Relacionamento: Composição
- -> Representa o pagamento da venda no qual o método faz parte.

---
### **Rules**

- Em desenvolvimento.

---
### Public Interface

- Em desenvolvimento

## Class: Movement

### **Responsibility**

- R -> Representar e registrar os movimentos realizados no sistema e fazer o controle do estoque dos produtos.

---
### **Relationships**

##### Sale
- Tipo de Relacionamento: Composição
- -> Representa um dos métodos de movimentação, saídas através de vendas.

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
### **Rules**

- Em desenvolvimento.

---
### Public Interface

- Em desenvolvimento