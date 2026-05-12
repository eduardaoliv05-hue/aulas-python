notas = [8.5, 6.0, 9.2, 4.5, 7.8, 5.5, 10.0, 3.0]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f"Notas:  {notas}")
print(f"Média:  {media:.1f}")
print(f"Maior:  {maior}")
print(f"Menor:  {menor}")
print(f"Soma:   {sum(notas)}")

# Classificando
aprovados  = [n for n in notas if n >= 7]
reprovados = [n for n in notas if n < 7]

print(f"\nAprovados ({len(aprovados)}):  {sorted(aprovados, reverse=True)}")
print(f"Reprovados ({len(reprovados)}): {sorted(reprovados)}")
print(f"Taxa de aprovação: {len(aprovados)/len(notas)*100:.0f}%")