a = float(input("digite o primeiro numero: "))
op = input("tipo de operacao: +, -, *, /: ")
b = float(input("digite o segundo numero: "))

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Erro: Divisão por zero invalida.")
else:
    print("Operação inválida.")