produtos = [
    {"codigo": "P001", "nome": "Camiseta",  "preco": 89.90},
    {"codigo": "P002", "nome": "Calça",     "preco": 159.90},
    {"codigo": "P003", "nome": "Tênis",     "preco": 249.90},
    {"codigo": "P004", "nome": "Boné",      "preco": 59.90},
]
procura = input("Digite o código do produto: ").upper()
for produto in produtos:
    if produto["codigo"] == procura:
        print(f"codigo buscado: {procura}\nProduto encontrado!\ncódigo: {produto['codigo']}\nnome: {produto['nome']}\nvalor: {produto['preco']:.2f} - R$")
    else:
        print(f"codigo buscado: {procura}\nProduto não encontrado!")