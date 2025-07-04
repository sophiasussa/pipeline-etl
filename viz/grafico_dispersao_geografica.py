import sys, os
sys.path.append(os.path.abspath("."))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from etl.extract import from_csv
from etl.transform import clean

def grafico_dispersao_geografica(df):
    geo_df = df[df['latitude'].notna() & df['longitude'].notna()]

    plt.figure(figsize=(10,6))
    sns.scatterplot(
        x='longitude', y='latitude',
        data=geo_df,
        hue='sigla_uf',
        palette='Set2',
        alpha=0.6,
        legend=False
    )
    plt.title('Distribuição geográfica de OSCs')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.tight_layout()
    plt.savefig('viz/imagem_dispersao_geografica.png')
    plt.show()
