-- =========================
-- STAGING: CUSTOMERS
-- =========================
DROP TABLE IF EXISTS staging.stg_customers;

SELECT 
    customer_id, 
    LOWER(TRIM(first_name)) AS first_name, 
    LOWER(TRIM(last_name)) AS last_name, 
    LOWER(email) AS email, 
    phone, 
    -- Note: INITCAP is not native in SQL Server, 
    -- usually handled with custom functions or STRING_AGG
    city, 
    country, 
    created_at 
INTO staging.stg_customers 
FROM raw.raw_customers;


-- =========================
-- STAGING: PRODUCTS
-- =========================
DROP TABLE IF EXISTS staging.stg_products;

SELECT
    product_id,
    TRIM(product_name) AS product_name,
    INITCAP(category) AS category,
    price,
    stock_quantity,
    is_active,
    created_at
INTO staging.stg_products
FROM raw.raw_products;


-- =========================
-- STAGING: ORDERS
-- =========================
DROP TABLE IF EXISTS staging.stg_orders;

SELECT
    order_id,
    customer_id,
    order_date,
    
    -- Normalize order status
    CASE 
        WHEN LOWER(order_status) IN ('completed', 'delivered') THEN 'completed'
        WHEN LOWER(order_status) IN ('pending') THEN 'pending'
        WHEN LOWER(order_status) IN ('processing') THEN 'processing'
        WHEN LOWER(order_status) IN ('cancelled', 'canceled') THEN 'cancelled'
        WHEN LOWER(order_status) IN ('returned') THEN 'returned'
        ELSE 'unknown'
    END AS order_status,

    total_amount,

    -- Normalize payment status
    CASE 
        WHEN LOWER(payment_status) IN ('paid', 'success') THEN 'paid'
        WHEN LOWER(payment_status) IN ('failed') THEN 'failed'
        WHEN LOWER(payment_status) IN ('unpaid') THEN 'unpaid'
        WHEN LOWER(payment_status) IN ('refunded') THEN 'refunded'
        ELSE 'unknown'
    END AS payment_status
into staging.stg_orders
FROM raw.raw_orders;


-- =========================
-- STAGING: ORDER ITEMS
-- =========================
DROP TABLE IF EXISTS staging.stg_order_items;

SELECT
    order_item_id,
    order_id,
    product_id,
    quantity,
    unit_price,
    line_total
INTO staging.stg_order_items
FROM raw.raw_order_items;


-- =========================
-- STAGING: PAYMENTS
-- =========================
DROP TABLE IF EXISTS staging.stg_payments;

SELECT
    payment_id,
    order_id,
    
    LOWER(payment_method) AS payment_method,

    CASE 
        WHEN LOWER(payment_status) IN ('success') THEN 'success'
        WHEN LOWER(payment_status) IN ('failed') THEN 'failed'
        WHEN LOWER(payment_status) IN ('refunded') THEN 'refunded'
        ELSE 'unknown'
    END AS payment_status,

    payment_amount,
    payment_date,
    transaction_reference
INTO staging.stg_payments
FROM raw.raw_payments;


-- =========================
-- STAGING: SHIPMENTS
-- =========================
DROP TABLE IF EXISTS staging.stg_shipments;

SELECT
    shipment_id,
    order_id,

    CASE 
        WHEN LOWER(shipment_status) IN ('processing') THEN 'processing'
        WHEN LOWER(shipment_status) IN ('shipped') THEN 'shipped'
        WHEN LOWER(shipment_status) IN ('delivered') THEN 'delivered'
        WHEN LOWER(shipment_status) IN ('returned') THEN 'returned'
        ELSE 'unknown'
    END AS shipment_status,

    INITCAP(carrier) AS carrier,
    tracking_number,
    shipped_date,
    delivered_date
INTO staging.stg_shipments
FROM raw.raw_shipments;