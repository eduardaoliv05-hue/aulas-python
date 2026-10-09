print("=== CONVERSOR DE TEMPERATURA ===")
try:
    temperatura = float(input("Digite a temperatura: "))
    print("\nEscolha a conversão:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
            resultado = (temperatura * 9/5) + 32
            print(f"{temperatura}°C = {resultado:.2f}°F")
    elif opcao == 2:
        resultado = (temperatura - 32) * 5/9
        print(f"{temperatura}°F = {resultado:.2f}°C")

    elif opcao == 3:
        resultado = temperatura + 273.15
        print(f"{temperatura}°C = {resultado:.2f} K")

    elif opcao == 4:
        resultado = temperatura - 273.15
        print(f"{temperatura} K = {resultado:.2f}°C")
    else:
        print("Opção inválida!")
except ValueError:
    print("Erro: digite apenas números válidos!")