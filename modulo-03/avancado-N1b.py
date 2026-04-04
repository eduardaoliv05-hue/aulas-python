peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)

print("====RESULTADO====")
if imc < 18.5:
    print(f"imc {imc:.2f}\nclassificação: Abaixo do peso")
elif imc < 25:
    print(f"imc {imc:.2f}\nclassificação: Peso normal")
elif imc < 30:
    print(f"imc {imc:.2f}\nclassificação: Sobrepeso")
else:
    print(f"imc {imc:.2f}\nclassificação: Obesidade")
print("=================")
print("Tabela IMC:\nAbaixo de 18.5  → Abaixo do peso\n18.5 a 24.9     → Peso Normal\n25.0 a 29.9     → Sobrepeso\n30.0 ou mais    → Obesidade")