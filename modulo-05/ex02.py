numeros = [3,1,7,4,5]

for n in sorted(numeros, reverse=True):#ordena os números do maior para o menor
    if n % 2 == 0:
        print(n)