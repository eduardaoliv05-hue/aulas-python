linhas = int(input("Quantas linhas na pirâmide? "))
print("\nTriângulo:")
for i in range(1, linhas + 1):
    print("*" * i)
    
print("\nPirâmide:")
for i in range(1, linhas + 1):
    espacos = " " * (linhas - i)
    estrelas = "*" * (2 * i - 1)
    print(espacos + estrelas)