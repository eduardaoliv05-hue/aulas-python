n = 0
for i in range (1, 6):#linhas de 1 a 5
    for n in range(1, i+1):#quantidade de numeros na linha
        print(f"{n}", end="")#imprime o número e não quebra a linha
    print()#quebra de linha