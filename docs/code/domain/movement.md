# Class: Movement

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