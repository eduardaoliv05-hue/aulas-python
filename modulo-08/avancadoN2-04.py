class NomeInvalido(Exception):
    pass


class EmailInvalido(Exception):
    pass


class IdadeInvalida(Exception):
    pass


def cadastrar(nome, email, idade):

    try:
        if nome == "":
            raise NomeInvalido("O nome não pode ser vazio.")

        if "@" not in email or "." not in email:
            raise EmailInvalido("E-mail deve conter '@' e '.'")

        if idade < 0 or idade > 120:
            raise IdadeInvalida("Idade deve ser entre 0 e 120.")

        print(f"Cadastro realizado: {nome} | {email} | {idade} anos")

    except NomeInvalido as e:
        print(f"NomeInvalido: {e}")

    except EmailInvalido as e:
        print(f"EmailInvalido: {e}")

    except IdadeInvalida as e:
        print(f"IdadeInvalida: {e}")

nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

idade = input("Idade: ")

try:
    idade = int(idade)
except ValueError:
    print("A idade deve ser um número.")

cadastrar(nome, email, idade)