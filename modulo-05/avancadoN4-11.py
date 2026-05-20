pesquisa = [
    {"nome": "Ana",    "linguagens": ["Python", "JavaScript", "SQL"]},
    {"nome": "Bruno",  "linguagens": ["Python", "Java", "C++"]},
    {"nome": "Carlos", "linguagens": ["JavaScript", "TypeScript", "Python"]},
    {"nome": "Diana",  "linguagens": ["Python", "R", "SQL"]},
    {"nome": "Elena",  "linguagens": ["Java", "Kotlin", "Swift"]},
]
contagem = {}
for pessoa in pesquisa:
    for linguagem in pessoa["linguagens"]:
        if linguagem in contagem:
            contagem[linguagem] = contagem.get(linguagem, 0) + 1
        else:
            contagem[linguagem] = 1
print("=== LINGUAGENS MAIS CITADAS ===")
for palavra, qtd in sorted(contagem.items(), key=lambda x: x[1], reverse=True):
    print(f"  {palavra:<10}:{qtd} Votos")
print(f"\nLinguagem mais popular: {max(contagem, key=contagem.get)}")
print("\nResponsentes que citaram Python:")
for pessoa in pesquisa:
    for linguagem in pessoa["linguagens"]:
        if linguagem == "Python":
            print(f"  - {pessoa['nome']}")    