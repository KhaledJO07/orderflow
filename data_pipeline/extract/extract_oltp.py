from sqlalchemy import create_engine
import os
import pandas as pd

def get_oltp_engine():
    return create_engine(
        f"postgresql://{os.getenv('OLTP_DB_USER')}:{os.getenv('OLTP_DB_PASSWORD')}@"
        f"{os.getenv('OLTP_DB_HOST')}:{os.getenv('OLTP_DB_PORT')}/{os.getenv('OLTP_DB_NAME')}"
    )


def extract_table(table_name):
    engine = get_oltp_engine()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df