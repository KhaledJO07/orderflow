-- RAW LAYER

CREATE TABLE IF NOT EXISTS raw.raw_customers AS
SELECT * FROM public.customers WHERE 1=0;

CREATE TABLE IF NOT EXISTS raw.raw_products AS
SELECT * FROM public.products WHERE 1=0;

CREATE TABLE IF NOT EXISTS raw.raw_orders AS
SELECT * FROM public.orders WHERE 1=0;

CREATE TABLE IF NOT EXISTS raw.raw_order_items AS
SELECT * FROM public.order_items WHERE 1=0;

CREATE TABLE IF NOT EXISTS raw.raw_payments AS
SELECT * FROM public.payments WHERE 1=0;

CREATE TABLE IF NOT EXISTS raw.raw_shipments AS
SELECT * FROM public.shipments WHERE 1=0;