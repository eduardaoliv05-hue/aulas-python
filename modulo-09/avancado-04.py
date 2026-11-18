
import os
import shutil
from datetime import datetime


def criar_backup(arquivo_original):

    try:
        # Verifica se o arquivo existe
        if not os.path.exists(arquivo_original):
            print("Arquivo original não encontrado!")
            return

        # Obtém o nome e a extensão do arquivo
        nome, extensao = os.path.splitext(arquivo_original)

        # Gera o timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Cria o nome do backup
        arquivo_backup = f"{nome}_backup_{timestamp}{extensao}"

        # Copia o arquivo original
        shutil.copy2(arquivo_original, arquivo_backup)

        # Obtém o tamanho do backup em KB
        tamanho = os.path.getsize(arquivo_backup)
        tamanho_kb = tamanho / 1024

        # Gera a data e hora para o log
        data_log = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registra o backup no arquivo de log
        with open("backup.log", "a", encoding="utf-8") as log:
            log.write(
                f"{data_log} | {arquivo_original} → "
                f"{arquivo_backup} | {tamanho_kb:.1f} KB\n"
            )

        print(f"[OK] Backup criado: {arquivo_backup}")
        print("[OK] Log atualizado: backup.log")

    except OSError as erro:
        print(f"Erro ao realizar backup: {erro}")


criar_backup("dados.csv")
