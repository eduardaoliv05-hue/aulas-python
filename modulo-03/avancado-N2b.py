import random
escolhas = ["pedra", "papel", "tesoura"]
jogador = input("pedra, papel ou tesoura? ")
computador = random.choice(escolhas)
print(f"Computador escolheu: {computador}")
if jogador.lower() == "pedra":
    if computador == "pedra":
        print("empate!")
    elif computador == "papel":
        print("computador venceu!")
    else:
        print("jogador venceu!")
elif jogador.lower() == "papel":
    if computador == "pedra":
        print("jogador venceu!")
    elif computador == "papel":
        print("empate!")
    else:
        print("computador venceu!")
elif jogador.lower() == "tesoura":
    if computador == "pedra":
        print("computador venceu!")
    elif computador == "papel":
        print("jogador venceu")
    else:
        print("empate")