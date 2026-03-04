
# Pipeline ETL de OSCs (Organizações da Sociedade Civil) com Visualizações Interativas

Este projeto realiza um **pipeline ETL completo** utilizando dados públicos de  Organizações da Sociedade Civil (OSCs), disponíveis em: [https://mapaosc.ipea.gov.br](https://mapaosc.ipea.gov.br).

### Principais funcionalidades:

- Extração de dados a partir de CSV
- Limpeza e transformação com tratamento de nulos, datas, colunas booleanas, numéricas e padronização
- Carga dos dados para CSV, SQLite ou PostgreSQL
- Dashboard interativo com Streamlit para visualização rápida
- Gráficos e análises com matplotlib/seaborn e Metabase
- Testes automatizados com Pytest
- Containerização com Docker para facilitar a execução e o deploy

---

## 📁 Estrutura do Projeto

```
pipeline-etl/
│
├── app/                      # Interface visual do dashboard
│   └── dashboard.py          # Dashboard interativo com Streamlit
│
├── data/                     # Arquivos de entrada e saída
│   └── oscs.csv              # Base de dados original
│
├── docs/                     # Documentação gerada automaticamente (pdoc)
│
├── etl/                      # Módulos do pipeline
│   ├── extract.py            # Função de extração
│   ├── transform.py          # Funções de limpeza e padronização
│   └── load.py               # Funções para exportar dados (CSV, SQLite, PostgreSQL)
│
├── tests/                    # Testes automatizados com pytest
│
├── viz/                      # Gráficos auxiliares
│
├── main.py                   # Pipeline interativo com menu CLI
├── Dockerfile                # Container Docker para rodar o pipeline
├── requirements.txt          # Dependências do projeto
├── .env                      # Variáveis de ambiente (ex: DB_URL)
└── README.md                 # Este arquivo
```

---
## Exportações Suportadas

Você poderá escolher exportar os dados para:

- Arquivo CSV limpo (`data/oscs_limpo.csv`)
- Banco SQLite (`data/banco_oscs.db`)
- Banco PostgreSQL (usando a variável `DB_URL`)

---

## Visualizações com Matplotlib & Seaborn

Abaixo estão algumas análises feitas a partir dos dados tratados pelo pipeline ETL.

### Distribuição por Área de Atuação
![Distribuição por Área](viz/imagem_areas.png)

### Organizações fundadas por ano
![Ano de Fundação](viz/imagem_ano_fundacao.png)

### Top Naturezas Jurídicas
![Natureza Jurídica](viz/imagem_natureza_juridica.png)

### Dispersão Geográfica das OSCs
![Dispersão Geográfica](viz/imagem_dispersao_geografica.png)

---
## Visualizações do Streamlit

![Dashboard Streamlit](viz/streamlit.png)
![Dashboard Streamlit + Filtro UF](viz/streamlit_uf.png)

---

## Integração com Metabase

O projeto foi pensado para integração com Metabase:

- Após a carga no PostgreSQL, basta conectar o Metabase ao banco
- Crie dashboards, gráficos e análises com filtros (ex: por UF, por área da OSC etc.)

Exemplo de conexão:

```
Host: localhost
Porta: 5432
Usuário: postgres
Senha: sua_senha
Banco de dados: oscs_db
```

![Dashboard Metabase](viz/dashboard.png)

---

## Como Executar o Projeto

### 1. Requisitos

- Python 3.12+
- Docker (opcional, mas recomendado)
- PostgreSQL local (ou em nuvem)
- Metabase (opcional, para dashboards)

---

### 2. Executando Localmente (sem Docker)

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o arquivo `.env` com a URL do banco PostgreSQL (opcional):

```
DB_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

Execute o pipeline:

```bash
python main.py
```

---

### 3. Executando com Docker

**1. Gere a imagem Docker:**

```bash
docker build -t etl-oscs .
```

**2. Rode o pipeline:**

```bash
docker run --rm -it --env-file .env -v %cd%/data:/app/data etl-oscs
```
---
## Testes

Os módulos podem ser testados individualmente.
Exemplo com `pytest`:

```bash
pytest tests/
```

---

## Licença

Este projeto está sob a licença MIT.
