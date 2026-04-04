nota = float(input("nota: "))
frequencia = float(input("frequencia: "))
if nota >= 6.0 and frequencia >= 75:
    print("Aprovado")
elif nota <= 5.0 and frequencia >= 75:
    print("Recuperação")
elif nota >= 6.0 and frequencia < 75:
    print("Reprovado por falta")
else:
    print("Reprovado")