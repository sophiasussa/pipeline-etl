import sys, os
sys.path.append(os.path.abspath("."))

from etl.extract import from_csv
from etl.transform import clean

from viz.grafico_dispersao_geografica import grafico_dispersao_geografica
from viz.grafico_natureza_juridica import grafico_natureza_juridica
from viz.grafico_por_ano import grafico_por_ano
from viz.grafico_por_area import grafico_por_area

def main():
    print("Carregando e limpando os dados...")
    df = from_csv('data/oscs.csv')
    df = clean(df)

    print("Gerando gráficos...")
    grafico_por_ano(df)
    grafico_por_area(df)
    grafico_dispersao_geografica(df)
    grafico_natureza_juridica(df)

    print("Todos os gráticos foram gerados e salvos na pasta 'viz/'.")

if __name__ == "__main__":
    main()
