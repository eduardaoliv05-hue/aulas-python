def aplicar(lista, funcao):
	return [funcao(item) for item in lista] 
numeros = [1, 4, 9, 16, 25]
print(aplicar(numeros, lambda x: x ** 0.5))
print(aplicar(numeros, lambda x: x * 2))
print(aplicar(["ana", "bruno", "carlos"], str.upper))