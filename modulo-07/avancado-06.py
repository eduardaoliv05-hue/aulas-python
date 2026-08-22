
def gerar_email(nome, pedido, status, valor, data, empresa):
    template = """Olá, {nome}!

    Seu pedido #{pedido} foi {status}.
    Valor total: R$ {valor:.2f}
    Previsão de entrega: {data}.

    Obrigada pela preferência!
    Equipe {empresa}"""

    return template.format(
        nome=nome,
        pedido=pedido,
        status=status,
        valor=valor,
        data=data,
        empresa=empresa
    )


email = gerar_email(
    "Ana Lima",
    1042,
    "aprovado",
    149.90,
    "20/03/2024",
    "KEI Store"
)

print(email)