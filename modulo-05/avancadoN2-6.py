import math

pontos = [(3, 4), (1, 1), (6, 8), (0, 5), (2, 2)]
distancias = [math.sqrt(x**2 + y**2) for x, y in pontos]
for ponto, distancia in zip(sorted(pontos, key=lambda p: math.sqrt(p[0]**2 + p[1]**2)), sorted(distancias)):
    print(f"Ponto: {ponto} - Distância: {distancia:.2f}")