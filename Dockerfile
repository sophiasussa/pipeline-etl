FROM python:3.12

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos
COPY . .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando que roda o ETL
CMD ["python", "main.py"]
