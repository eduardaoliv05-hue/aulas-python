senha = input("Digite a senha: ")

if len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha):
    print("Senha forte:\n✅ Comprimento OK (10 caracteres)\n✅ Tem letras maiúsculas\n✅ Tem números")
elif len(senha) < 8 and not any(c.isupper() for c in senha) and not any(c.isdigit() for c in senha): 
    print("senha invalida:\n❌ Muito curta (mínimo 8 caracteres)\n❌ Sem letras maiúsculas\n❌ Sem números")
elif len(senha) >= 6:
    print("senha fraca(mínimo 8 caracteres)")
elif not any(c.isupper() for c in senha):
    print("senha fraca: deve conter pelo menos uma letra maiúscula")
elif not any(c.isdigit() for c in senha):
    print("senha fraca: deve conter pelo menos um número")