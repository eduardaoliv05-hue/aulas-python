produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "estoque": 10,
    "disponivel": True
}

print("Antes:", produto)

# Aplicar desconto de 15%
produto["preco"] = produto["preco"] * 0.85

# Atualizar estoque
produto["estoque"] -= 3

# Adicionar novo campo
produto["garantia_meses"] = 12

# Verificar e remover campo
if "disponivel" in produto:
    del produto["disponivel"]

print("Depois:", produto)
print(f"Preço com desconto: R$ {produto['preco']:.2f}")