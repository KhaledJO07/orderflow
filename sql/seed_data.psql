-- =========================
-- CUSTOMERS
-- =========================
INSERT INTO customers (first_name, last_name, email, phone, city, country)
VALUES
('Khaled', 'Jokhadar', 'khaled.jokhadar@example.com', '+96170000001', 'Beirut', 'Lebanon'),
('Sara', 'Haddad', 'sara.haddad@example.com', '+96170000002', 'Tripoli', 'Lebanon'),
('Omar', 'Nasser', 'omar.nasser@example.com', '+96170000003', 'Sidon', 'Lebanon'),
('Lina', 'Farah', 'lina.farah@example.com', '+96170000004', 'Jounieh', 'Lebanon'),
('Youssef', 'Karam', 'youssef.karam@example.com', '+96170000005', 'Zahle', 'Lebanon'),
('Maya', 'Saliba', 'maya.saliba@example.com', '+96170000006', 'Byblos', 'Lebanon'),
('Ali', 'Hamdan', 'ali.hamdan@example.com', '+96170000007', 'Tyre', 'Lebanon'),
('Nour', 'Khoury', 'nour.khoury@example.com', '+96170000008', 'Aley', 'Lebanon');

-- =========================
-- PRODUCTS
-- =========================
INSERT INTO products (product_name, category, price, stock_quantity, is_active)
VALUES
('Wireless Mouse', 'Electronics', 25.99, 120, TRUE),
('Mechanical Keyboard', 'Electronics', 79.99, 80, TRUE),
('USB-C Charger', 'Electronics', 19.50, 150, TRUE),
('Laptop Stand', 'Accessories', 34.99, 60, TRUE),
('Noise Cancelling Headphones', 'Electronics', 149.99, 40, TRUE),
('Office Chair', 'Furniture', 199.99, 20, TRUE),
('Notebook Set', 'Stationery', 12.99, 200, TRUE),
('Desk Lamp', 'Furniture', 45.00, 50, TRUE),
('Backpack', 'Accessories', 59.90, 70, TRUE),
('Water Bottle', 'Lifestyle', 15.75, 100, TRUE);

-- =========================
-- ORDERS
-- =========================
INSERT INTO orders (customer_id, order_date, order_status, total_amount, payment_status)
VALUES
(1, '2026-03-01 10:15:00', 'completed', 105.98, 'paid'),
(2, '2026-03-02 14:30:00', 'completed', 149.99, 'paid'),
(3, '2026-03-03 09:45:00', 'cancelled', 79.99, 'failed'),
(1, '2026-03-05 16:20:00', 'completed', 215.74, 'paid'),
(4, '2026-03-06 11:10:00', 'processing', 34.99, 'paid'),
(5, '2026-03-07 13:40:00', 'shipped', 244.99, 'paid'),
(6, '2026-03-08 18:05:00', 'completed', 38.98, 'paid'),
(7, '2026-03-09 12:00:00', 'pending', 59.90, 'unpaid'),
(8, '2026-03-10 15:15:00', 'completed', 61.74, 'paid'),
(2, '2026-03-12 17:25:00', 'returned', 25.99, 'refunded');

-- =========================
-- ORDER ITEMS
-- =========================
INSERT INTO order_items (order_id, product_id, quantity, unit_price, line_total)
VALUES
-- Order 1
(1, 1, 1, 25.99, 25.99),
(1, 2, 1, 79.99, 79.99),

-- Order 2
(2, 5, 1, 149.99, 149.99),

-- Order 3
(3, 2, 1, 79.99, 79.99),

-- Order 4
(4, 4, 1, 34.99, 34.99),
(4, 6, 1, 199.99, 199.99),
(4, 10, 1, 15.75, 15.75),

-- Order 5
(5, 4, 1, 34.99, 34.99),

-- Order 6
(6, 6, 1, 199.99, 199.99),
(6, 8, 1, 45.00, 45.00),

-- Order 7
(7, 3, 2, 19.50, 39.00),

-- Order 8
(8, 9, 1, 59.90, 59.90),

-- Order 9
(9, 7, 2, 12.99, 25.98),
(9, 10, 1, 15.75, 15.75),
(9, 1, 1, 25.99, 25.99),

-- Order 10
(10, 1, 1, 25.99, 25.99);

-- =========================
-- PAYMENTS
-- =========================
INSERT INTO payments (order_id, payment_method, payment_status, payment_amount, payment_date, transaction_reference)
VALUES
(1, 'credit_card', 'success', 105.98, '2026-03-01 10:20:00', 'TXN100001'),
(2, 'paypal', 'success', 149.99, '2026-03-02 14:35:00', 'TXN100002'),
(3, 'credit_card', 'failed', 79.99, '2026-03-03 09:50:00', 'TXN100003'),
(4, 'credit_card', 'success', 215.74, '2026-03-05 16:25:00', 'TXN100004'),
(5, 'cash_on_delivery', 'success', 34.99, '2026-03-06 11:15:00', 'TXN100005'),
(6, 'paypal', 'success', 244.99, '2026-03-07 13:45:00', 'TXN100006'),
(7, 'credit_card', 'success', 38.98, '2026-03-08 18:10:00', 'TXN100007'),
(9, 'credit_card', 'success', 61.74, '2026-03-10 15:20:00', 'TXN100008'),
(10, 'credit_card', 'refunded', 25.99, '2026-03-12 17:30:00', 'TXN100009');

-- =========================
-- SHIPMENTS
-- =========================
INSERT INTO shipments (order_id, shipment_status, carrier, tracking_number, shipped_date, delivered_date)
VALUES
(1, 'delivered', 'DHL', 'TRK100001', '2026-03-02 08:00:00', '2026-03-04 15:30:00'),
(2, 'delivered', 'Aramex', 'TRK100002', '2026-03-03 09:00:00', '2026-03-05 13:20:00'),
(4, 'delivered', 'LibanPost', 'TRK100003', '2026-03-06 10:00:00', '2026-03-09 17:00:00'),
(5, 'processing', 'DHL', 'TRK100004', NULL, NULL),
(6, 'shipped', 'Aramex', 'TRK100005', '2026-03-08 14:00:00', NULL),
(7, 'delivered', 'DHL', 'TRK100006', '2026-03-09 09:00:00', '2026-03-11 16:00:00'),
(9, 'delivered', 'LibanPost', 'TRK100007', '2026-03-11 10:30:00', '2026-03-13 12:45:00'),
(10, 'returned', 'DHL', 'TRK100008', '2026-03-13 08:00:00', '2026-03-16 14:10:00');