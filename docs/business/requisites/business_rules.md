- # **Regras de negócio.**
---
-	**Vendas**
	RNGV01 - Uma venda só poderá ser concluída quando o total dos pagamentos for igual ao valor total da venda.
	RNGV02 - Uma venda deverá ser cancelada caso o estoque não permitir a retirada de um produto.
	RNGV03 - Qualquer produto adicionado a uma venda vira com só podera ter valores acima de 0.
	RNGV04 - Uma venda é iniciada quando é adicionado um produto.
	RNGV05 - Os descontos serão aplicados na venda inteira, não em produtos individualmente.
---
-	**Estoque**
	RNGE01 - Uma movimentação deve ser barrada sempre que a quantidade requisitada não estiver disponível.
	RNGE02 - A quantidade de um produto nunca pode ser negativa.
	RNGE03 - Saídas manuais devem ser registradas o motivo.
	RNGE04 - Os produtos não podem ser excluídos para haver persistência no sistema. Neste caso, apenas desativá-los.
---
-	**User**
	RNGU01
