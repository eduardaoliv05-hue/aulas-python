quantidade = int(input("Quantos produtos vou cadastrar? "))
produtos = []

for i in range(quantidade):
    nome = input(f"Nome do produto {i + 1}: ")
    produtos.append(nome)

print(f"\n=== {len(produtos)} PRODUTOS CADASTRADOS ===")
for i, p in enumerate(sorted(produtos), 1):
    print(f"  {i}. {p}")