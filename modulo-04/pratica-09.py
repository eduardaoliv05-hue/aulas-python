n = int(input("Quantos números você quer digitar? ")) #4
maior = None
menor = None
for i in range(n):
    numero = float(input(f"Número {i + 1}: ")) #5\2\8\3
    
    if maior is None or numero > maior: #true\false\true\false
        maior = numero #5->8
    if menor is None or numero < menor:
        menor = numero#2

print(f"\nMaior: {maior}")
print(f"Menor: {menor}")
print(f"Diferença: {maior - menor:.2f}")