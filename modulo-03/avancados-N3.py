notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input("digite o valor do saque: "))
for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    print(f"{quantidade} X de R$ {nota}")

# 150\100 = 1
# 150%100 = 50
# 50\50 = 1
# 50%50 = 0