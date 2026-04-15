from extract.extract_oltp import extract_incremental
from load.load_raw import get_max_id, load_to_raw

TABLE_CONFIG = {
    "customers": "customer_id",
    "products": "product_id",
    "orders": "order_id",
    "order_items": "order_item_id",
    "payments": "payment_id",
    "shipments": "shipment_id"
}


def run():
    for table, id_col in TABLE_CONFIG.items():
        print(f"Processing {table}...")

        last_id = get_max_id(table, id_col)

        df = extract_incremental(table, id_col, last_id)

        if df.empty:
            print(f"No new data for {table}")
            continue

        load_to_raw(df, table)

        print(f"Loaded {len(df)} new rows into raw_{table}")
        
if __name__ == "__main__":
    run()