from extract.extract_oltp import extract_table
from load.load_raw import load_to_raw

TABLES = [
    "customers",
    "products",
    "orders",
    "order_items",
    "payments",
    "shipments"
]


def run():
    for table in TABLES:
        print(f"Processing {table}...")

        df = extract_table(table)
        load_to_raw(df, table)

        print(f"Loaded {len(df)} rows into raw_{table}")


if __name__ == "__main__":
    run()