print("=== CAIXA REGISTRADORA ===")
total = 0
count = 0
desconto = 0
while True:
    valor = input("Digite o valor do item (0 para finalizar): R$ ")
    if valor == "0":
        break
    else:
        total += float(valor)
        count += 1
        print(f"Item {count}: R$ {valor}")
print()
print("=============================")
if total > 50.00:
    desconto = total * 0.6
print(f"total de itens: {count}")
print()
print(f"subtotal: R$ {total:.2f}\nDesconto: R$ {desconto:.2f}\nTOTAL: R$ {total - desconto:.2f}")
pago = float(input("Valor pago: R$ "))
troco = pago - (total - desconto)
print(f"Troco: R$ {troco:.2f}")