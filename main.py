from etl.extract import from_csv
from etl.transform import clean
from etl.load import to_csv

def run():
    df = from_csv('data/oscs.csv')
    df_limpo = clean(df)
    to_csv(df_limpo, 'data/oscs_limpo.csv')

    if __name__ == "__main__":
        run()
