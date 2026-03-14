preco_unitario = 10.50
quantidade = 20
desconto = 0.5
total = preco_unitario * quantidade
total_com_desconto = total - (total * desconto)
print(f"total sem desconto: R$ {total:.2f}")
print(f"total com desconto: R$ {total_com_desconto:.2f}")