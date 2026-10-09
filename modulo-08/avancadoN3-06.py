registros = [
    {"nome": "Ana",    "idade": "28",  "salario": "3500.00"},
    {"nome": "Bruno",  "idade": "abc", "salario": "2800.00"},
    {"nome": "",       "idade": "35",  "salario": "4200.00"},
    {"nome": "Diana",  "idade": "29",  "salario": "nao_sei"},
    {"nome": "Elena",  "idade": "31",  "salario": "5100.00"},
]

sucesso = 0
erros = 0

print("=== IMPORTANDO REGISTROS ===")

for registro in registros:

    try:
        nome = registro["nome"]
        idade = int(registro["idade"])
        salario = float(registro["salario"])

        if nome == "":
            raise ValueError("nome não pode ser vazio")

        print(f"[OK]    {nome:<7} | {idade} anos | R$ {salario:.2f}")
        sucesso += 1

    except ValueError as e:
        erros += 1

        if registro["nome"] == "":
            print(f"[ERRO]  (vazio)| {e}")
        elif registro["idade"] == "abc":
            print(f"[ERRO]  {registro['nome']:<7} | idade inválida: '{registro['idade']}'")
        else:
            print(f"[ERRO]  {registro['nome']:<7} | salário inválido: '{registro['salario']}'")

    except Exception as e:
        erros += 1
        print(f"[ERRO]  {registro['nome']:<7} | erro inesperado: {e}")

print()
print("=== RESUMO ===")
print(f"Processados: {len(registros)}  |  Sucesso: {sucesso}  |  Erros: {erros}")