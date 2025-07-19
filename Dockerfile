FROM python:3.12

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY requirements.txt ./
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o Streamlit apontando para seu script
CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
