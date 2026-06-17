def somar(a, b):    return a + b
def subtrair(a, b):    return a - b
def multiplicar(a, b):    return a * b
def dividir (a, b):
    if b == 0:
        return "divisao por zero."
    return a / b
def calcular (a, operacao, b):
    operacoes ={"+": somar, "-": subtrair, "*": multiplicar, "/": dividir}
    if operacao in operacoes:
        return operacoes[operacao](a, b)
    return "Operação inválida."

a = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
b = float(input("Digite o segundo número: "))
print (f"resultado: {calcular(a, operacao, b)}")