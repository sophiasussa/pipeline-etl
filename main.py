from etl.extract import from_csv
from etl.transform import clean
from etl.load import to_csv, to_sqlite

def run():
    df = from_csv('data/oscs.csv')
    df_limpo = clean(df)

    # Exporta para CSV
    to_csv(df_limpo, 'data/oscs_limpo.csv')

    # Exporta para banco SQLite
    to_sqlite(df_limpo, 'data/banco_oscs.db', 'oscs')

if __name__ == "__main__":
    run()
