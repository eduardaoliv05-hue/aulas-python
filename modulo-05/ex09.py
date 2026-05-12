lista_com_repeticoes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print(f"Original ({len(lista_com_repeticoes)}): {lista_com_repeticoes}")

# Eliminar duplicatas preservando ordem
vistos = set()
sem_repeticao = []
for item in lista_com_repeticoes:
    if item not in vistos:
        sem_repeticao.append(item)
        vistos.add(item)

print(f"Sem repetição ({len(sem_repeticao)}): {sem_repeticao}")
print(f"Itens únicos (sorted): {sorted(sem_repeticao)}")

# Exemplo com turmas
turma_manha = {"Ana", "Bruno", "Carlos", "Diana"}
turma_tarde  = {"Carlos", "Diana", "Eduardo", "Flávia"}

print(f"\nEm ambas as turmas: {turma_manha & turma_tarde}")
print(f"Só de manhã: {turma_manha - turma_tarde}")
print(f"Total de alunos: {len(turma_manha | turma_tarde)}")#| é a união dos conjuntos, ou seja, todos os alunos sem repetição