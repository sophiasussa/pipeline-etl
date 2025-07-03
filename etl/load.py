import pandas as pd
from sqlalchemy import create_engine
import logging

def to_csv(df: pd.DataFrame, output_path: str):
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Dados exportados com sucesso para: {output_path}")
    except Exception as e:
        logging.error(f"Erro ao exportar CSV: {e}")

def to_sqlite(df: pd.DataFrame, db_path: str, table_name: str):
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Tabela '{table_name}' salva com sucesso em {db_path}")
    except Exception as e:
        logging.error(f"Erro ao salvar no banco SQLite: {e}")

def to_postgresql(df: pd.DataFrame, db_url: str, table_name: str):
    """
    Salva DataFrame em uma tabela PostgreSQL.
    """
    try:
        engine = create_engine(db_url)
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Tabela '{table_name}' salva com sucesso no PostgreSQL")
    except Exception as e:
        logging.error(f"Erro ao salvar no PostgreSQL: {e}")
