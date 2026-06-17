def medidas():
	print("1. fahrenheit")
	print("2. celsius")
	print("3. kelvin")
	print("4. sair")
def converter_fahrenheit(c):return (c * 9/5) + 32
def converter_celsius(f):    return (f - 32) * 5/9
def converter_kelvin(c):    return c + 273.15

while True:
	medidas()
	opcao = input("escolha uma opcaum")
	if opcao == "1":
		c = float(input("temperatura em celsius"))
		print(f"resultado: {converter_fahrenheit(c)}")
	elif opcao == "2":
		f = float(input("temperatura em fahrenheit: "))
		print(f"resultado: {converter_celsius(f)}")
	elif opcao == "3":
		c = float(input("temperatura em celsius: "))
		print(f"resultado: {converter_kelvin(c)}")
	elif opcao == "4":
		break
	else:
		print("opcao invalida")