import pytest
import pandas as pd
from etl.extract import from_csv

def test_from_csv_valido():
    df = from_csv('data/oscs.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_from_csv_incexistente():
    df = from_csv('data/inexistente.csv')
    assert df.empty
