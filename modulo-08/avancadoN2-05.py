def conectar_banco(consulta):
    print("[INFO] Abrindo conexão com o banco...")

    try:
        print(f"[INFO] Executando consulta: {consulta}")

        if consulta == "SELECT * FROM usuarios":
            raise Exception("Tabela 'usuarios' não encontrada.")

        print("[OK] 3 registros encontrados.")

    except Exception as e:
        print(f"[ERRO] {e}")

    finally:
        print("[INFO] Fechando conexão.")


conectar_banco("SELECT * FROM usuarios")
print()
conectar_banco("SELECT * FROM produtos")