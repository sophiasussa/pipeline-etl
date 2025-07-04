import sys, os
sys.path.append(os.path.abspath("."))

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from etl.extract import from_csv
from etl.transform import clean

def grafico_por_area(df):
    colunas_area = [col for col in df.columns if col.startswith('area_')]

    contagem = df[colunas_area].sum().sort_values(ascending=False)
    contagem.index = [col.replace('area_', '').replace("_", " ").title() for col in contagem.index]

    plt.figure(figsize=(12,6))
    plt.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribuição das OSCs por Área de Atuação')
    plt.tight_layout()
    plt.savefig('viz/imagem_areas.png')
    plt.show()
