alunos  = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
notas_1 = [8.0, 5.5, 9.5, 7.0, 6.0]
notas_2 = [7.5, 6.0, 8.5, 8.0, 5.5]
notas_3 = [9.0, 7.0, 9.0, 6.5, 7.0]
aprovados =0
recuperacao=0
print()
print("=== BOLETIM ESCOLAR ===") 
print(f"{"N°":<3}{"Nome":<10}{'N1':<5}{"N2":<5}{"N3":<5}{"Media":<7}Situação") 
for i, (nome, n1, n2, n3) in enumerate(zip(alunos, notas_1, notas_2, notas_3), 1):
    media = (n1 + n2 + n3) / 3
    if media >= 7.0:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        recuperacao += 1
    print(f"{i:<3}{nome:<10}{n1:<5}{n2:<5}{n3:<5}{media:<7.2f}{situacao}")
print(f"\nTotal de aprovados: {aprovados}\nRecuperaçâo {recuperacao}")