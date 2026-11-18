
import csv


def cadastrar_alunos():
    alunos = [
        {"nome": "Ana Lima", "email": "ana@email.com", "nota": 8.5},
        {"nome": "Bruno Costa", "email": "bruno@email.com", "nota": 6.0},
        {"nome": "Carlos Melo", "email": "carlos@email.com", "nota": 9.2}
    ]

    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:

        campos = ["nome", "email", "nota"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(alunos)

    print("Alunos cadastrados com sucesso!")


def gerar_relatorio():
    alunos = []

    with open("alunos.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for aluno in leitor:
            aluno["nota"] = float(aluno["nota"])
            alunos.append(aluno)

    print("\n=== RELATÓRIO DE ALUNOS ===")

    total_notas = 0
    aprovados = 0
    reprovados = 0

    for aluno in alunos:

        nome = aluno["nome"]
        email = aluno["email"]
        nota = aluno["nota"]

        total_notas += nota

        if nota >= 7:
            situacao = "Aprovado"
            aprovados += 1
        else:
            situacao = "Reprovado"
            reprovados += 1

        print(f"{nome:<13} | {email:<17} | {nota:.1f} | {situacao}")

    if len(alunos) > 0:
        media = total_notas / len(alunos)
        print(f"\nMédia da turma: {media:.1f}")

    print(f"Aprovados: {aprovados} | Reprovados: {reprovados}")


cadastrar_alunos()
gerar_relatorio()
