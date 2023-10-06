import pandas as pd
from .database_connector import connect_to_db


def convert_date_format(df, date_column):
    df[date_column] = pd.to_datetime(df[date_column]).dt.strftime("%Y%m%d")
    return df


def load_and_save(table_name, connection):
    query = f"SELECT * FROM {table_name};"
    data = pd.read_sql(query, connection)

    # Convertendo o formato da coluna dat_nasc para alunos
    if table_name == "alunos" and "dat_nasc" in data.columns:
        data = convert_date_format(data, "dat_nasc")

    data.to_csv(f"data/{table_name}.csv", index=False)
    return data
