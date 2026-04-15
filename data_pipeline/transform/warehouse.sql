DROP TABLE IF EXISTS analytics.dim_customers;

SELECT DISTINCT
    customer_id,
    first_name,
    last_name,
    email,
    city,
    country,
    created_at
INTO analytics.dim_customers
FROM staging.stg_customers;


DROP TABLE IF EXISTS analytics.dim_products;

SELECT DISTINCT
    product_id,
    product_name,
    category,
    price,
    is_active
INTO analytics.dim_products
FROM staging.stg_products;


DROP TABLE IF EXISTS analytics.dim_dates;

SELECT DISTINCT
    DATE(order_date) AS date,
    EXTRACT(YEAR FROM order_date) AS year,
    EXTRACT(MONTH FROM order_date) AS month,
    EXTRACT(DAY FROM order_date) AS day,
    EXTRACT(DOW FROM order_date) AS day_of_week
INTO analytics.dim_dates
FROM staging.stg_orders;


DROP TABLE IF EXISTS analytics.fact_orders;

SELECT
    o.order_id,
    o.customer_id,
    DATE(o.order_date) AS order_date,
    o.order_status,
    o.payment_status,
    o.total_amount
INTO analytics.fact_orders
FROM staging.stg_orders o;



DROP TABLE IF EXISTS analytics.fact_order_items;

SELECT
    oi.order_item_id,
    oi.order_id,
    oi.product_id,
    oi.quantity,
    oi.unit_price,
    oi.line_total
INTO analytics.fact_order_items
FROM staging.stg_order_items oi;