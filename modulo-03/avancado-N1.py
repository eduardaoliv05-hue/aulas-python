x = 15 #imprime "grande"
if x > 10:
    print("grande")
elif x > 5:
    print("médio")
else:
    print("pequeno")

nota = 7.0 #imprime "B"
if nota >= 9:
    print("A")
elif nota >= 7:
    print("B")
elif nota >= 5:
    print("C")
else:
    print("D")

idade = 18 #imprime "Precisa de documento"
tem_id = False

if idade >= 18 and tem_id:
    print("Pode entrar")
elif idade >= 18:
    print("Precisa de documento")
else:
    print("Menor de idade")