import sys, os
sys.path.append(os.path.abspath("."))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from etl.extract import from_csv
from etl.transform import clean

def grafico_natureza_juridica(df):
    contagem_nat = df['codigo_natureza_juridica'].value_counts().head(5)
    contagem_nat.index = contagem_nat.index.astype(str)

    plt.figure(figsize=(10,6))
    sns.barplot(x=contagem_nat.values, y=contagem_nat.index, palette='viridis')
    plt.title('Top Naturezas Jurídicas das OSCs')
    plt.xlabel('Quantidade')
    plt.ylabel('Código Natureza Jurídica')
    plt.tight_layout()
    plt.savefig('viz/imagem_natureza_juridica.png')
    plt.show()
