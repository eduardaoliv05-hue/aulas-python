def validar_nota (nota):
    if 0 <= nota <= 10:
        return True
    return False

def classificar_nota (nota):
    if not validar_nota(nota):
        return "Nota inválida"
    if nota >= 9: return "A"
    elif nota >= 7: return "B"
    elif nota >= 5: return "C"
    else: return "D"

nota = float(input("Digite a nota: "))
print(f"classificação: {classificar_nota(nota)}")