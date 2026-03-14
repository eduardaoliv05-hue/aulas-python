capital_inicial = float(input("Digite o valor do capital inicial: "))
juros = float(input("Digite a taxa de juros mensal (em %): "))
periodo = int(input("Digite o período de investimento (em meses): "))
porcentagem_rendimento_total = ((capital_inicial * (1 + juros / 100) ** periodo - capital_inicial) / capital_inicial) * 100

print("===simulação de investimento===")
print(f"capital inicial: R${capital_inicial:.2f}")
print(f"taxa mensal: {juros}%")
print(f"período: {periodo} meses")
print(f"\nMontante final: R${capital_inicial * (1 + juros / 100) ** periodo:.2f}")
print(f"rendimento : R${capital_inicial * (1 + juros / 100) ** periodo - capital_inicial:.2f}")
print(f"rendimento total: {porcentagem_rendimento_total:.2f}%")