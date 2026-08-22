import datetime

vendas = [
    {"data": "2024-01-05", "produto": "Camiseta", "valor": 89.90},
    {"data": "2024-01-18", "produto": "Calça", "valor": 149.90},
    {"data": "2024-02-03", "produto": "Tênis", "valor": 299.90},
    {"data": "2024-02-20", "produto": "Boné", "valor": 59.90},
    {"data": "2024-03-10", "produto": "Meia", "valor": 29.90}
]

vendas_por_mes = {}

for venda in vendas:

    data = datetime.datetime.strptime(venda["data"], "%Y-%m-%d")
    mes = data.strftime("%m/%Y")
    vendas_por_mes[mes] = vendas_por_mes.get(mes, [])
    vendas_por_mes[mes].append(venda)


print("=== RELATÓRIO DE VENDAS ===")

total_geral = 0

for mes, lista_vendas in vendas_por_mes.items():

    subtotal = 0

    print(f"\n{mes}")

    for venda in lista_vendas:
        print(f"  {venda['produto']}    R$ {venda['valor']:.2f}")

        subtotal += venda["valor"]

    print(f"  Subtotal: R$ {subtotal:.2f}")

    total_geral += subtotal


print(f"\nTOTAL GERAL: R$ {total_geral:.2f}")