from etl import extract, transform, load

def main():
    print("🔍 Iniciando extração...")
    raw_data = extract.from_csv("data/oscs.csv")
    print("✅ Extração concluída.")

    print("🧼 Iniciando transformação...")
    clean_data = transform.clean(raw_data)
    print("✅ Transformação concluída.")

    print("📦 Iniciando carga...")
    load.to_database(clean_data)
    print("✅ Dados carregados com sucesso no SQLite.")

if __name__ == "__main__":
    main()
