import random
print()
print("=== TORNEIO CODE ===")
Times = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby', 'Go', 'Rust', 'Swift']
rodadas = ["Quartas de Final", "Semifinais", "Final"]
partidas = 0
while len(Times) > 1:
    print(f"\n--- {rodadas[partidas]} ---")
    random.shuffle(Times)#embarablha uma lista
    vencedores = []
    for i in range(0, len(Times), 2):#vai de 2 em 2 para pegar os times
        time1 = Times[i]
        time2 = Times[i + 1]
        gol1 = random.randint(0, 5)
        gol2 = random.randint(0, 5)
        print(f"{time1} {gol1} x {gol2} {time2}", end="")
        if gol1 > gol2:
            print(f" -> {time1} avança!")
            vencedores.append(time1)
        elif gol2 > gol1:
            print(f" -> {time2} avança!")
            vencedores.append(time2)
        else:
            vencedor = random.choice([time1, time2])
            print(f" -> Decidido nos penaltis... {vencedor} avança!")
            vencedores.append(vencedor)
    Times = vencedores
    partidas += 1
print(f"\n=== O CAMPEÃO É: {Times[0]}! ===")