import pandas as pd
import logging

def to_csv(df: pd.DataFrame, output_path: str):
    try:
        df.to_csv(output_path, index=False)
        logging.info(f"Dados exportados com sucesso para: {output_path}")
    except Exception as e:
        logging.error(f"Erro ao exportar CSV: {e}")
