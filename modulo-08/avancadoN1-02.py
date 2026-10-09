def calculadora(valor1, operador, valor2):

    try:
        numero1 = float(valor1)
    except ValueError:
        print(f'Erro: "{valor1}" não é um número válido.')
        return None

    try:
        numero2 = float(valor2)
    except ValueError:
        print(f'Erro: "{valor2}" não é um número válido.')
        return None

    if operador == "+":
        resultado = numero1 + numero2

    elif operador == "-":
        resultado = numero1 - numero2

    elif operador == "*":
        resultado = numero1 * numero2

    elif operador == "/":
        try:
            resultado = numero1 / numero2
        except ZeroDivisionError:
            print("Erro: não é possível dividir por zero.")
            return None

    else:
        print(f'Erro: operação "{operador}" não suportada.')
        return None

    print(f"Resultado: {resultado}")

numero1 = input("Digite o primeiro número: ")
operador = input("Digite o operador (+, -, *, /): ")
numero2 = input("Digite o segundo número: ")
calculadora(numero1, operador, numero2)