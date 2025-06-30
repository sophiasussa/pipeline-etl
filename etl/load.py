from sqlalchemy import create_engine

def to_database(dataframe):
    engine = create_engine('sqlite:///database/oscs.db')
    
    dataframe.to_sql('oscs', con=engine, if_exists='replace', index=False)
