turma_A = {"Ana", "Bruno", "Carlos", "Diana", "Elena"}
turma_B = {"Bruno", "Felipe", "Diana", "Gustavo", "Helena"}

print(f"Só da turma A: {turma_A - turma_B}")#- é a diferença dos conjuntos, ou seja, os alunos que estão apenas na turma A
print(f"Só da turma B: {turma_B - turma_A}")
print(f"Em ambas as turmas: {turma_A & turma_B}")#& é a interseção dos conjuntos, ou seja, os alunos que estão em ambas as turmas
print(f"Total de alunos: {len(turma_A | turma_B)}")#| é a união dos conjuntos, ou seja, todos os alunos sem repetição