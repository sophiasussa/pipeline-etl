import pandas as pd
from sqlalchemy import create_engine, inspect
from etl.load import to_postgresql
from dotenv import load_dotenv
import os

load_dotenv()

def test_to_postgresql():
    db_url = os.getenv("DB_URL")
    assert db_url is not None, "DB_URL não encontrado. Verifique o .env."
    table_name = 'teste_oscs'

    df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'idade': [28, 34],
        'ativo': [True, False]
    })

    to_postgresql(df, db_url, table_name)

    engine = create_engine(db_url)
    inspector = inspect(engine)
    assert table_name in inspector.get_table_names()

    df_lido = pd.read_sql_table(table_name, con=engine)
    pd.testing.assert_frame_equal(df_lido, df, check_dtype=False)
