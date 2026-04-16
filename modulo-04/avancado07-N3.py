print()
numeros = input("Digite números separados por espaço: ").split()
lista = [int(x) for x in numeros.split()]
ordenada = sorted(lista)#ordena a lista do menor para o maior
quantidade = len(lista)
soma = sum(lista)
media = soma / quantidade
maior = max(lista)
menor = min(lista)
pos_maior= 0
pos_menor =0
for i,n in enumerate(numeros, 1):
    if n == maior:
        pos_maior = i
    if n == menor:
        pos_menor = i
pares = [n for n in lista if n % 2 == 0]
impares = [n for n in lista if n % 2 != 0]
acima_media = [n for n in lista if n > media]
print()
print("=== ANÁLISE DA SEQUÊNCIA ===")
print(f"numeros: {lista}")
print(f"ordenada: {ordenada}")
print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior} (posição {pos_maior})")
print(f"Menor: {menor} (posição {pos_menor})")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
print(f"Acima da média: {acima_media}")