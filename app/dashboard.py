import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from etl.extract import from_csv
from etl.transform import clean
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados e aplicar transformações
@st.cache_data
def load_data():
    df_raw = from_csv('data/oscs.csv')
    return clean(df_raw)

df_original = load_data()

# Título e filtro por UF
st.title("Dashboard de OSCs")
uf_selecionada = st.selectbox(
    'Selecione o Estado (UF):',
    options=['Todos'] + sorted(df_original['sigla_uf'].dropna().unique().tolist())
)
df = df_original if uf_selecionada == 'Todos' else df_original[df_original['sigla_uf'] == uf_selecionada]

st.write(f"Mostrando {len(df)} registros.")

# Indicadores principais
total_osc = len(df)
ano_medio = int(df['dt_fundacao'].dt.year.mean()) if df['dt_fundacao'].notna().any() else "N/A"
fundacao_mais_antiga = df['dt_fundacao'].min().strftime("%Y-%m-%d") if df['dt_fundacao'].notna().any() else "N/A"
uf_mais_comum = df['sigla_uf'].value_counts().idxmax()

colunas_subarea = [col for col in df.columns if col.startswith("subarea_")]
subarea_mais_comum = "N/A"
if colunas_subarea:
    contagem_sub = df[colunas_subarea].sum()
    if not contagem_sub.empty:
        subarea_mais_comum = contagem_sub.idxmax().replace("subarea_", "").replace("_", " ").title()

col1, col2 = st.columns(2)
col1.metric("Total de OSCs", total_osc)
col2.metric("Ano Médio de Fundação", ano_medio)

col3, col4 = st.columns(2)
col3.metric("Fundação Mais Antiga", fundacao_mais_antiga)
col4.markdown(f"""
    <div style="text-align:left">
        Subárea Mais Comum<br>
        <span style="font-size:18px;">{subarea_mais_comum}</span>
    </div>
""", unsafe_allow_html=True)


# Função: gráfico de fundação
def grafico_fundacao(df):
    df = df[df['dt_fundacao'].notna()]
    df['ano_fundacao'] = df['dt_fundacao'].dt.year
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(df['ano_fundacao'], bins=30, kde=False, color='skyblue', ax=ax)
    ax.set_title("Quantidade de OSCs fundadas por ano")
    ax.set_xlabel("Ano de fundação")
    ax.set_ylabel("Quantidade")
    st.pyplot(fig)

# Função: gráfico de pizza por área
def grafico_areas(df):
    colunas_area = [col for col in df.columns if col.startswith('area_')]
    contagem = df[colunas_area].sum().sort_values(ascending=False)
    contagem.index = [col.replace('area_', "").replace("_", " ").title() for col in contagem.index]
    fig2, ax2 = plt.subplots(figsize=(7,7))
    ax2.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=140)
    ax2.set_title("Distribuição das OSCs por Área de Atuação")
    st.pyplot(fig2)

# Abas
tab1, tab2 = st.tabs(["Gráficos", "Tabela"])

with tab1:
    st.subheader("Gráficos de Análise")
    grafico_fundacao(df)
    grafico_areas(df)

with tab2:
    st.subheader("Tabela de Dados")
    if uf_selecionada == 'Todos':
        st.warning("Selecione uma UF para visualizar a tabela. O conjunto completo é muito grande.")
    else:
        st.dataframe(df)

    # Botão para baixar CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar CSV filtrado",
        data=csv,
        file_name="oscs_filtradas.csv",
        mime='text/csv'
    )
