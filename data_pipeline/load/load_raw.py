import psycopg2
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_dw_engine():
    return create_engine(
        f"postgresql://{os.getenv('DW_DB_USER')}:{os.getenv('DW_DB_PASSWORD')}@"
        f"{os.getenv('DW_DB_HOST')}:{os.getenv('DW_DB_PORT')}/{os.getenv('DW_DB_NAME')}"
    )


def load_to_raw(df, table_name):
    engine = get_dw_engine()

    df.to_sql(
        name=f"raw_{table_name}",
        con=engine,
        schema="raw",
        if_exists="append",
        index=False
    )