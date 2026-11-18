
import csv
import os
from datetime import date

ARQUIVO = "tarefas.csv"


# 1. Carregar tarefas do arquivo CSV
def carregar_tarefas():
    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            return [
                {
                    "id": int(linha["id"]),
                    "descricao": linha["descricao"],
                    "data": linha["data"],
                    "prioridade": linha["prioridade"],
                    "concluida": linha["concluida"] == "True"
                }
                for linha in leitor
            ]

    except FileNotFoundError:
        return []


# 2. Salvar tarefas no arquivo CSV
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["id", "descricao", "data", "prioridade", "concluida"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(tarefas)


# 3. Adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")

    print("Prioridade:")
    print("1. Alta")
    print("2. Média")
    print("3. Baixa")

    opcao = input("Escolha: ")

    prioridades = {
        "1": "Alta",
        "2": "Média",
        "3": "Baixa"
    }

    if opcao not in prioridades:
        print("Prioridade inválida!")
        return

    if not descricao.strip():
        print("A descrição não pode ficar vazia!")
        return

    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    tarefa = {
        "id": novo_id,
        "descricao": descricao,
        "data": date.today().isoformat(),
        "prioridade": prioridades[opcao],
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada com sucesso!")


# 4. Listar tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for tarefa in tarefas:
        status = "[x]" if tarefa["concluida"] else "[ ]"

        print(
            f'{status} #{tarefa["id"]} | '
            f'{tarefa["descricao"]} | '
            f'{tarefa["data"]} | '
            f'{tarefa["prioridade"]}'
        )

    concluidas = sum(1 for t in tarefas if t["concluida"])
    pendentes = len(tarefas) - concluidas

    print(
        f"\nTotal: {len(tarefas)} tarefas | "
        f"Concluídas: {concluidas} | "
        f"Pendentes: {pendentes}"
    )


# 5. Concluir uma tarefa
def concluir_tarefa(tarefas):
    try:
        identificador = int(input("ID da tarefa: "))
    except ValueError:
        print("Digite um número válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == identificador:
            tarefa["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída!")
            return

    print("Tarefa não encontrada.")


# 6. Remover uma tarefa
def remover_tarefa(tarefas):
    try:
        identificador = int(input("ID da tarefa que deseja remover: "))
    except ValueError:
        print("Digite um número válido!")
        return

    for tarefa in tarefas:
        if tarefa["id"] == identificador:
            tarefas.remove(tarefa)
            salvar_tarefas(tarefas)
            print("Tarefa removida!")
            return

    print("Tarefa não encontrada.")


# 7. Menu principal
def main():
    tarefas = carregar_tarefas()

    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("0. Sair")

        opcao = input("\nOpção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
