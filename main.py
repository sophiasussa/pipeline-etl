from etl import extract, transform, load

def main():
    raw_data = extract.from_csv("data/oscs.csv")
    clean_data = transform.clean(raw_data)
    load.to_database(clean_data)

if __name__ == "__main__":
    main()
