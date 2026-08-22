from datetime import date

nascimento_str = input("Data de nascimento (DD/MM/AAAA): ")
partes = nascimento_str.split("/")
nascimento = date(int(partes[2]), int(partes[1]), int(partes[0]))

hoje = date.today()
dias = (hoje - nascimento).days #.days retorna a diferença em dias entre duas datas
anos = dias // 365 #// faz a divisão inteira, descartando o resto

print(f"Você tem {anos} anos ({dias} dias vividos)")