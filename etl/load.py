from sqlalchemy import create_engine

def to_database(df):
    engine = create_engine("sqlite:///database/oscs.db")  # ou outro banco
    df.to_sql("oscs", con=engine, if_exists="replace", index=False)
