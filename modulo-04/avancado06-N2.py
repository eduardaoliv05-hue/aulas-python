print()
print("Coletando 5 notas válidas (0 a 10):")
notas = []
while len(notas) < 5:
    nota= float(input(f"nota {len(notas)+1}/5: "))
    try:
         nota = float(nota)
    except ValueError:
        print("Entrada inválida. Digite um número entre 0 e 10.")
        continue
    if 0 > nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        continue
    notas.append(nota)
    print("nota registrada!")
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
print()
print("=== RESULTADO ===")
print(f"Notas: {notas}\nMédia: {media:.2f}\nMaior nota: {maior:.2f}\nMenor nota: {menor:.2f}")