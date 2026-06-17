import random


def gerar_numero():
    return random.randint(1, 10)


def pedir_palpite():
    return int(input("Adivinhe o número (1 a 10): "))

def verificar_palpite(numero, palpite):
    if numero == palpite:
        return "acertou"
    elif numero < palpite:
        return "menor"
    else:
        return "maior"


def jogar():
    numero = gerar_numero()
    tentativas = 3
    while tentativas > 0:
        palpite = pedir_palpite()
        resultado = verificar_palpite(numero, palpite)
        if resultado == "acertou":
            print("🎉 Parabéns! Você acertou o número!")
            break
        if resultado == "menor":
            print("🔻 O número é menor.")
        else:
            print("🔺 O número é maior.")
        tentativas -= 1
        if tentativas == 0:
            print(
                f"❌ Você perdeu! As tentativas acabaram.o numero era {numero}.")
            break


jogar()
