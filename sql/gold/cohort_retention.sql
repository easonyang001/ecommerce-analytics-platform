CREATE OR REPLACE VIEW gold_cohort_retention AS
SELECT
  DATE_FORMAT(MIN(o.order_purchase_timestamp), '%Y-%m') AS cohort,
  DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
  COUNT(DISTINCT o.customer_id) AS customers
FROM orders o
GROUP BY o.customer_id, month;
