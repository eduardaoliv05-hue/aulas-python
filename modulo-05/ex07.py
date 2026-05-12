alunos = [
    {"nome": "Ana",    "nota1": 8.0, "nota2": 9.0},
    {"nome": "Bruno",  "nota1": 5.5, "nota2": 6.0},
    {"nome": "Carlos", "nota1": 7.5, "nota2": 8.5},
    {"nome": "Diana",  "nota1": 4.0, "nota2": 5.0},
    {"nome": "Eduardo","nota1": 9.5, "nota2": 9.0},
]

# Calcular média de cada aluno e definir situação
for a in alunos:
    a["media"] = (a["nota1"] + a["nota2"]) / 2
    a["situacao"] = "Aprovado" if a["media"] >= 7 else "Reprovado"

# Exibir relatório
print(f"\n{'Nome':<10} {'N1':>5} {'N2':>5} {'Média':>7} {'Situação'}")
print("-" * 40)
for a in alunos:
    print(f"{a['nome']:<10} {a['nota1']:>5.1f} {a['nota2']:>5.1f} {a['media']:>7.1f}  {a['situacao']}")

# Estatísticas
medias = [a["media"] for a in alunos]
print(f"\nMédia da turma: {sum(medias)/len(medias):.1f}")
print(f"Melhor aluno: {max(alunos, key=lambda a: a['media'])['nome']}")