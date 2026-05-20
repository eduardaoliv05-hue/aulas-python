alunos = [
    {"nome": "Ana",    "notas": [8.0, 7.5, 9.0, 8.5]},
    {"nome": "Bruno",  "notas": [5.0, 6.0, 5.5, 7.0]},
    {"nome": "Carlos", "notas": [9.5, 8.0, 9.0, 10.0]},
    {"nome": "Diana",  "notas": [6.5, 7.0, 6.0, 5.5]},
]
media = lambda notas: sum(notas) / len(notas)
for a in alunos:
    a["media"] = media(a["notas"])
    a["situacao"] = "Aprovado" if a["media"] >= 7.0 else "Reprovado"
print("=== BOLETIM ESCOLAR ===")
for a in alunos:
    print(f"{a['nome']:<10}| Media: {a['media']:<7.1f} | Situação: {a['situacao']}")
print("\n=== RANKING ===")
alunos.sort(key=lambda a: a["media"], reverse=True)
for i, a in enumerate(alunos, 1):
    print(f"{i}. {a['nome']} - {a['media']:.1f}")