def validar_email(email):

    erros = []

    if not email.count("@")== 1:

        erros.append("invalido!(sem @)")

    usuario = email.split("@")
    if usuario[0] == "":

        erros.append("invalido!(sem usuario)")

    if "." not in usuario[1]:

        erros.append("invalido!(sem dominio)")

    if len(usuario[1]) <2:

        erros.append("extenção muito curta")

    return erros

  

while True:

    email = input("crie um email: ")

    erros = validar_email(email)

  

    if not erros:

        print("✅email  válido!")

        break

    else:

        for erro in erros:

            print(f" - {erro}")