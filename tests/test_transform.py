import pandas as pd
from etl.transform import clean

def test_clean_colunas_renomeadas():
    df = pd.DataFrame({
        'tx_razao_social_osc': ['Teste'],
        'tx_latitude': [10.0],
        'tx_longitude': [20.0],
        'dt_fundacao_osc': ['01/02/2000']
    })
    df_limpo = clean(df)
    assert 'razao_social' in df_limpo.columns
    assert 'latitude' in df_limpo.columns
    assert pd.api.types.is_datetime64_any_dtype(df_limpo['dt_fundacao'])
    