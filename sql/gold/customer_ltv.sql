CREATE TABLE gold_customer_ltv AS
SELECT
  c.customer_id,
  c.customer_city,
  SUM(p.payment_value) AS lifetime_value,
  COUNT(DISTINCT o.order_id) AS orders
FROM silver_customers c
JOIN silver_orders o
  ON c.customer_id = o.customer_id
JOIN silver_payments p
  ON o.order_id = p.order_id
GROUP BY
  c.customer_id,
  c.customer_city;
