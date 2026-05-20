texto = "AAABBBCCDDDD"

resultado = ""
contador = 1
    #3         4
for i in range(1, len(texto)):# Começa a partir do segundo caractere para comparar com o anterior
    if texto[i] == texto[i - 1]:
        contador += 1
    else:
        resultado += texto[i - 1] + str(contador)
        contador = 1

resultado += texto[-1] + str(contador)

print("Texto comprimido:")
print(resultado)
