print("=== SISTEMA DE NOTAS ===")
try:
    quantidade = int(input("Quantas notas você deseja informar? "))

    if quantidade <= 0:
        raise ValueError("A quantidade de notas deve ser maior que zero.")
    notas = []
    for i in range(quantidade):
        while True:
            try:
                nota = float(input(f"Digite a {i + 1}ª nota: "))
                if nota < 0 or nota > 10:
                    raise ValueError("A nota deve estar entre 0 e 10.")
                notas.append(nota)
                break
            except ValueError as erro:
                print(f"Erro: {erro}")
                print("Digite a nota novamente.")
    media = sum(notas) / len(notas)
    print("\n=== RESULTADO ===")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    if media >= 9:
        print("Classificação: Excelente")

    elif media >= 7:
        print("Classificação: Bom")

    elif media >= 5:
        print("Classificação: Regular")

    else:
        print("Classificação: Reprovado")
except ValueError as erro:
    print(f"Erro: {erro}")

            
