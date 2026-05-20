notas = [7.5, 8.0, 6.5, 9.2, 5.0, 8.8, 7.0, 4.5, 9.5, 6.0]
quantidade = len(notas)
maior = max(notas)
menor = min(notas)
media = sum(notas) / quantidade
aprovados  = [n for n in notas if n >= 7] #[VALOR for ITEM in LISTA]
reprovados = [n for n in notas if n < 7]
print(f"quantidade de notas: {quantidade}")
print(f"maior nota: {maior}")
print(f"menor nota: {menor}")
print(f"média: {media}")
print(f"aprovados: {len(aprovados)}")
print(f"reprovados: {len(reprovados)}")
