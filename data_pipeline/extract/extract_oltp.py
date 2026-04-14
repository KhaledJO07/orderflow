import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def get_oltp_connection():
    return psycopg2.connect(
        host=os.getenv("OLTP_DB_HOST"),
        port=os.getenv("OLTP_DB_PORT"),
        database=os.getenv("OLTP_DB_NAME"),
        user=os.getenv("OLTP_DB_USER"),
        password=os.getenv("OLTP_DB_PASSWORD")
    )


def extract_table(table_name):
    conn = get_oltp_connection()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df