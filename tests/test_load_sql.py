import pandas as pd
from sqlalchemy import create_engine
from etl.load import to_sqlite

def test_to_sqlite(tmp_path):
    df = pd.DataFrame({
        'nome': ['Alice', 'Bob'],
        'idade': [30, 25],
        'ativo': [True, False],
        'salario': [5000.0, 3000.0]
    })

    db_path = tmp_path / "teste.db"

    to_sqlite(df, str(db_path), "pessoas")

    engine = create_engine(f'sqlite:///{db_path}')
    df_lido = pd.read_sql_table("pessoas", con=engine)

    pd.testing.assert_frame_equal(df_lido, df, check_dtype=False)
