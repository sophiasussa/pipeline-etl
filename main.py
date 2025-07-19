from etl.extract import from_csv
from etl.transform import clean
from etl.load import to_csv, to_sqlite, to_postgresql
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

load_dotenv()
DB_URL = os.getenv("DB_URL")

def run_pipeline():
    df = from_csv('data/oscs.csv')
    df_limpo = clean(df)
    return df_limpo

def menu():
    print("\n===Pipeline ETL ===")
    print("1 - Exportar para CSV")
    print("2 - Exportar para SQLite")
    print("3 - Exportar para ambos")
    print("4 - Exportar para PostgreSQL")
    print("0 - Sair")

def executar_opcao(opcao, df_limpo):
    if opcao == '1':
        to_csv(df_limpo, 'data/oscs_limpo.csv')
    elif opcao == '2':
        to_sqlite(df_limpo, 'data/banco_oscs.db', 'oscs')
    elif opcao == '3':
        to_csv(df_limpo, 'data/oscs_limpo.csv')
        to_sqlite(df_limpo, 'data/banco_oscs.db', 'oscs')
    elif opcao == '4':
        if not DB_URL:
            logging.error("Variável DB_URL não encontrada. Verifique o .env.")
        else:
            df_limpo = df_limpo.sample(n=100, random_state=42)
            to_postgresql(df_limpo, DB_URL, 'oscs')
    elif opcao == '0':
        print("Encerrando...")
    else:
        print("Opção invalida. Tente novamente.")

def run():
    df_limpo = run_pipeline()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '0':
            executar_opcao(opcao, df_limpo)
            break
        executar_opcao(opcao, df_limpo)

if __name__ == "__main__":
    run()
