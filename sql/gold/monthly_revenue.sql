CREATE OR REPLACE VIEW gold_monthly_revenue AS
SELECT
  DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
  SUM(p.payment_value) AS revenue
FROM orders o
JOIN payments p ON o.order_id = p.order_id
WHERE o.order_purchase_timestamp IS NOT NULL
GROUP BY month
ORDER BY month;
