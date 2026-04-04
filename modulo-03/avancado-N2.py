estado = input('estado destino: ')
peso = float(input('peso da encomenda (kg): '))
valor = input("compra acima de R$ 200? (s/n): ")
frete = 0
dias = 0
if valor.lower() == 's' and estado.upper() == 'SP' or estado == 'RJ':
    frete = 0
    if estado.upper() == 'SP':
        dias = 3
    else:
        dias = 4
elif estado.upper() == 'SP':
    frete = peso * 5.00
    dias = 3
elif estado.upper() == 'RJ':
    frete = peso * 6.00
    dias = 4
elif estado.upper() == 'MG':
    frete = peso * 7.00
    dias = 5
else:
    frete = peso * 10.00
    dias = 8
print(
    f"======CALCULO DO FRETE======\nDestino: {estado.upper()}\nPeso: {peso} kg\nfrete base: R$ {frete:.2f}")
if valor.lower() == 's' and estado.upper() == 'SP' or estado.upper() == 'RJ':
    print(f"Desconto: R$ {frete:.2f}\nFrete final: R$ 0.00")
else:
    print("Desconto: R$ 0.00")
    print(f"Frete final: R$ {frete:.2f}")
print(f"Prazo de entrega: {dias} dias uteis")