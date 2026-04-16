import random
print("=== ADIVINHE O NÚMERO (1 a 100) ===")
tentativas = 7
count = 1
numero = random.randint(1, 100)
while tentativas >0:
    chute = int(input(f"vece tem {tentativas} tentativas. digite seu chute: "))
    if chute == numero:
        print(f"Parabéns! Você acertou em {count} tentativas! O número era {numero}!")
        break
    elif chute < numero:
        print(f"Tentativa {count}\nMaior! restam {tentativas - 1} tentativas.")
    else:
        print(f"Tentativa {count}\nMenor! restam {tentativas - 1} tentativas.")
    print()
    tentativas -= 1
    count += 1
if tentativas == 0:
    print(f"Game Over! O número era {numero}.\n Voce usou Todas as tentativas.")