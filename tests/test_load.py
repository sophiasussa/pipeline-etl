import pandas as pd
from etl.load import to_csv

def test_to_csv_salva_arquivo(tmp_path):
    df = pd.DataFrame({
        'coluna1': [1,2,3],
        'coluna2': ['a', 'b', 'c']
    })

    arquivo_csv = tmp_path / "saida.csv"

    to_csv(df, str(arquivo_csv))

    df_lido = pd.read_csv(arquivo_csv)

    pd.testing.assert_frame_equal(df, df_lido)
