import sys, os
sys.path.append(os.path.abspath("."))

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from etl.extract import from_csv
from etl.transform import clean

def grafico_por_ano(df):
    # Gráfico de barras: Organizações fundadas por ano
    df = df[df['dt_fundacao'].notna()]
    df['ano_fundacao'] = df['dt_fundacao'].dt.year
    plt.figure(figsize=(12, 6))
    sns.histplot(df['ano_fundacao'], bins=30, kde=False, color='skyblue')
    plt.title("Quantidade de OSCs fundadas por ano")
    plt.xlabel("Ano de fundação")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('viz/imagem_ano_fundacao.png')
    plt.show()
