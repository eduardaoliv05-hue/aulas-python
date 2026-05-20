produtos = [
    ("Maçã", "Fruta"),
    ("Leite", "Laticínio"),
    ("Banana", "Fruta"),
    ("Queijo", "Laticínio"),
    ("Uva", "Fruta"),
    ("Iogurte", "Laticínio"),
    ("Manga", "Fruta"),
]

grupo = {}
for produto, categoria in produtos:
    grupo.setdefault(categoria, []).append(produto)
for categoria, itens in grupo.items():
    print(f"{categoria}: {itens}")
