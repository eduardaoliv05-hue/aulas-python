conta = float(input("digite o valor da conta: "))
gorjeta = float(input("digite a porcentagem da gorjeta: "))
valor_gorjeta = conta * gorjeta / 100
pessoas = int(input("digite o número de pessoas: "))

print("===conta dividida===")
print(f"valor total da conta: R${conta:.2f}")
print(f"valor da gorjeta ({gorjeta}%): R${conta * gorjeta / 100:.2f}")
print(f"total com gorjeta: R${valor_gorjeta + conta:.2f}")
print(f"valor por pessoa: R${(valor_gorjeta + conta) / pessoas:.2f}")