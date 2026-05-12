# Simula um estoque com lista de dicionários
estoque = [
    {"nome": "Caneta",   "preco": 2.50,  "qtd": 100},
    {"nome": "Caderno",  "preco": 15.90, "qtd": 30},
    {"nome": "Borracha", "preco": 1.20,  "qtd": 80},
    {"nome": "Régua",    "preco": 3.80,  "qtd": 0},
    {"nome": "Lápis",    "preco": 1.50,  "qtd": 55},
]

print("=== RELATÓRIO DE ESTOQUE ===\n")
valor_total = 0

for produto in estoque:
    valor = produto["preco"] * produto["qtd"]
    valor_total += valor
    status = "⚠️ ESGOTADO" if produto["qtd"] == 0 else f"{produto['qtd']} un."
    print(f"{produto['nome']:<12} R${produto['preco']:>6.2f}  {status:<12}  Valor: R${valor:>8.2f}")

print(f"\n{'─'*55}")
print(f"Valor total em estoque: R$ {valor_total:.2f}")
print(f"Produtos disponíveis: {len([p for p in estoque if p['qtd'] > 0])}/{len(estoque)}")
print(f"Produto mais caro: {max(estoque, key=lambda p: p['preco'])['nome']}")
print(f"Produto mais barato: {min(estoque, key=lambda p: p['preco'])['nome']}")