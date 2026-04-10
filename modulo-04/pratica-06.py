n = int(input("Digite um número para calcular o fatorial: ")) #3
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i   # 1* 1 = 1
                    # 1* 2 = 2
                    # 2* 3 = 6

print(f"{n}! = {fatorial}")