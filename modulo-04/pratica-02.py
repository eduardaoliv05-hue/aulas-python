while True:
    idade = input("Digite sua idade: ")
    
    if idade.isdigit() and int(idade) > 0:
        print(f"Idade registrada: {int(idade)} anos")
        break
    else:
        print("Entrada inválida! Tente novamente.")