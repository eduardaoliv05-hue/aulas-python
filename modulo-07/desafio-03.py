from datetime import datetime

vendas = [
    ("Produto A", 3, 25.90),
    ("Produto B", 1, 149.00),
    ("Produto C", 5, 12.50),
]

total_geral = sum(qtd * preco for item, qtd, preco in vendas)

print(f"\n{'=' * 45}")
print(f"  RELATÓRIO DE VENDAS")
print(f"  Emitido em: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print(f"{'=' * 45}")
print(f"{'PRODUTO':<20} {'QTD':>5} {'UNITÁRIO':>10} {'TOTAL':>10}")
print(f"{'-' * 45}")

for nome, qtd, preco in vendas:
    subtotal = qtd * preco
    print(f"{nome:<20} {qtd:>5} {preco:>10.2f} {subtotal:>10.2f}")

print(f"{'=' * 45}")
print(f"{'TOTAL GERAL':>36} {total_geral:>8.2f}")