bases = [2, 3, 5, 7, 10]

print(f"\n{'Base':<6} {'²':>6} {'³':>6} {'⁴':>6} {'⁵':>6}") #:<n para definir quantos espaços a palavra ocupará, alinhada à direita.
print("-" * 34)

for i, base in enumerate(bases, 1):
    print(f"{i}. {base:<4} {base**2:>6} {base**3:>6} {base**4:>6} {base**5:>6}")