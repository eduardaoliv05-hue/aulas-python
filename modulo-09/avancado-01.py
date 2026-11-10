
from datetime import datetime

def adicionar_entrada():
    nota = input("Digite sua nota: ")

    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M")

    entrada = f"[{data_hora}] {nota}\n"

    with open("diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(entrada)

    print(entrada.strip())
    print("Entrada salva com sucesso!")


def listar_entradas():
    try:
        with open("diario.txt", "r", encoding="utf-8") as arquivo:
            entradas = arquivo.readlines()

        print(f"\n=== MEU DIÁRIO ({len(entradas)} entradas) ===")

        for entrada in entradas:
            print(entrada.strip())

    except FileNotFoundError:
        print("Seu diário ainda está vazio!")


def main():
    while True:
        print("\n=== MEU DIÁRIO ===")
        print("1 - Adicionar entrada")
        print("2 - Listar entradas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_entrada()

        elif opcao == "2":
            listar_entradas()

        elif opcao == "3":
            print("Encerrando o diário...")
            break

        else:
            print("Opção inválida!")


main()

