CREATE OR REPLACE VIEW gold_customer_ltv AS
SELECT
  c.customer_id,
  c.customer_city,
  SUM(p.payment_value) AS lifetime_value,
  COUNT(DISTINCT o.order_id) AS orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
GROUP BY c.customer_id, c.customer_city;
