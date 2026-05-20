estoque = {
    "camiseta": 20,
    "calça": 15,
    "tênis": 8,
    "meia": 50,
    "boné": 6,
}
print("=== ESTOQUE ===")
for produto, quantidade in estoque.items():
    print(f"{produto}: {quantidade} Unidades")
vendas = [
    ("camiseta", 17),
    ("calça", 12),
    ("tênis", 5),
    ("boné", 4),
]
print("\n=== ESTOQUE ATUALIZADO ===")
for produto, vendido in vendas:
        if produto in estoque:
            estoque[produto] -= vendido
for produto, quantidade in estoque.items():
        if estoque[produto] < 5:
            print(f"{produto:<10}: {estoque[produto]:<3} Unidades   ⚠️ ESTOQUE BAIXO")
        else:
            print(f"{produto:<10}: {estoque[produto]:<3} Unidades")