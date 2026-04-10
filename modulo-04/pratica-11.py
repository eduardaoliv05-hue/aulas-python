palavra = input("Digite uma palavra: ").lower().strip() #.strip() remove os espaços em branco no início e no final
invertida = ""
for letra in palavra:
    invertida = letra + invertida 
if palavra == invertida:
    print(f"'{palavra}' É um palíndromo!")
else:
    print(f"'{palavra}' NÃO é um palíndromo.")
    print(f"Invertida: '{invertida}'")