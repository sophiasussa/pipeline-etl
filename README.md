# ETL Pipeline for CSOs (Civil Society Organizations) with Interactive Visualizations

This project implements a **complete ETL pipeline** using public data from Civil Society Organizations (CSOs), available at: [https://mapaosc.ipea.gov.br](https://mapaosc.ipea.gov.br).

### Key Features:
- Data extraction from CSV files
- Cleaning and transformation with handling of null values, dates, boolean columns, numeric fields, and standardization
- Data loading to CSV, SQLite, or PostgreSQL
- Interactive Streamlit dashboard for quick visualization
- Charts and analyses with matplotlib/seaborn and Metabase
- Automated testing with Pytest
- Containerization with Docker for easy execution and deployment

---

## Project Structure

```
pipeline-etl/
│
├── app/                      # Dashboard visual interface
│   └── dashboard.py          # Interactive dashboard with Streamlit
│
├── data/                     # Input and output files
│   └── oscs.csv              # Original dataset
│
├── docs/                     # Auto-generated documentation (pdoc)
│
├── etl/                      # Pipeline modules
│   ├── extract.py            # Extraction function
│   ├── transform.py          # Cleaning and standardization functions
│   └── load.py               # Functions for exporting data (CSV, SQLite, PostgreSQL)
│
├── tests/                    # Automated tests with pytest
│
├── viz/                      # Auxiliary charts
│
├── main.py                   # Interactive pipeline with CLI menu
├── Dockerfile                # Docker container to run the pipeline
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables (e.g., DB_URL)
└── README.md                 # This file
```

---

## Supported Export Formats

You can choose to export data to:
- Clean CSV file (`data/oscs_limpo.csv`)
- SQLite database (`data/banco_oscs.db`)
- PostgreSQL database (using the `DB_URL` variable)

---

## Visualizations with Matplotlib & Seaborn

Below are some analyses generated from data processed by the ETL pipeline.

### Distribution by Area of Activity
![Distribution by Area](viz/imagem_areas.png)

### Organizations Founded per Year
![Year of Foundation](viz/imagem_ano_fundacao.png)

### Top Legal Natures
![Legal Nature](viz/imagem_natureza_juridica.png)

### Geographic Dispersion of CSOs
![Geographic Dispersion](viz/imagem_dispersao_geografica.png)

---

## Streamlit Visualizations

![Streamlit Dashboard](viz/streamlit.png)
![Streamlit Dashboard + State Filter](viz/streamlit_uf.png)

---

## Metabase Integration

The project was designed for integration with Metabase:
- After loading data into PostgreSQL, simply connect Metabase to the database
- Create dashboards, charts, and analyses with filters (e.g., by state, by CSO area, etc.)

Example connection settings:
```
Host: localhost
Port: 5432
User: postgres
Password: your_password
Database: oscs_db
```

![Metabase Dashboard](viz/dashboard.png)

---

## How to Run the Project

### 1. Requirements
- Python 3.12+
- Docker (optional, but recommended)
- PostgreSQL (local or cloud)
- Metabase (optional, for dashboards)

---

### 2. Running Locally (without Docker)

Install the dependencies:
```bash
pip install -r requirements.txt
```

Create the `.env` file with the PostgreSQL database URL (optional):
```
DB_URL=postgresql://user:password@localhost:5432/database_name
```

Run the pipeline:
```bash
python main.py
```

---

### 3. Running with Docker

**1. Build the Docker image:**
```bash
docker build -t etl-oscs .
```

**2. Run the pipeline:**
```bash
docker run --rm -it --env-file .env -v %cd%/data:/app/data etl-oscs
```

---

## Tests

Modules can be tested individually.

Example with `pytest`:
```bash
pytest tests/
```

---

## License

This project is licensed under the MIT License.
