import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    return idade

def fim_do_ano():
    hoje = datetime.date.today()
    fim_ano = datetime.date(hoje.year, 12, 31)
    return (fim_ano - hoje).days

def noventa_dias():
    hoje = datetime.date.today()
    noventa_dias = hoje + datetime.timedelta(days=90) #timedelta é uma classe que representa a diferença entre duas datas ou horários
    return noventa_dias

def dia_semana():
    hoje = datetime.date.today()
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    return dias_semana[hoje.weekday()] #weekday() retorna o índice do dia da semana (0 para segunda-feira, 6 para domingo)

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento = datetime.datetime.strptime(
    data_nascimento,
    "%d/%m/%Y"
).date()

print("Idade:", calcular_idade(data_nascimento), "anos")
print("Dias até o fim do ano:", fim_do_ano(), "dias")
print("Data daqui 90 dias:", noventa_dias())
print("Dia da semana:", dia_semana())