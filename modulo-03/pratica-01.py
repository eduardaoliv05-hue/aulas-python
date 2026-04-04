idade = int(input("Digite a idade: "))
if idade <= 0:
    print("Idade inválida.")
elif idade < 18:
    print("Menor de idade, entrada proibida")
else:
    print("Maior de idade, entrada permitida")