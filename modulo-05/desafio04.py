alunos = []
quantidade = int(input("quantidade de alunos: "))
for _ in range(quantidade):
    nome = input("nome do aluno: ")
    nota1 = float(input("primeira nota: "))
    nota2 = float(input("segunda nota: "))
    alunos.append({"nome": nome, "nota1": nota1, "nota2": nota2})

for a in alunos:
    a["media"] = (a["nota1"] + a["nota2"]) / 2
    a["situacao"] = "Aprovado" if a["media"] >= 7 else "Reprovado"

print(f"\n{'Nome':<10} {'N1':>5} {'N2':>5} {'Média':>7} {'Situação'}")
print("-" * 40)
for a in alunos:
    print(f"{a['nome']:<10} {a['nota1']:>5.1f} {a['nota2']:>5.1f} {a['media']:>7.1f}  {a['situacao']}")

medias = [a["media"] for a in alunos]
print(f"\nMédia da turma: {sum(medias)/len(medias):.1f}")
print(f"Melhor aluno: {max(alunos, key=lambda a: a['media'])['nome']}")