def camada(inicio, fim, largura_max):
    for i in range(inicio, fim):
        estrelas = 2 *i +1
        espacos = (largura_max - estrelas) // 2
        print(" " * espacos + "*" * estrelas)
altura = 4
largura_max = altura *5 -1
camada(0, altura, largura_max)
camada(1, altura+1, largura_max)
camada(2, altura+2, largura_max)
for _ in range(2):
    print(" " * (largura_max // 2) +"|")
