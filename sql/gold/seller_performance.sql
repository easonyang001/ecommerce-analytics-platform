CREATE OR REPLACE VIEW gold_seller_performance AS
SELECT
  s.seller_id,
  s.seller_city,
  s.seller_state,
  SUM(oi.price) AS sales,
  COUNT(DISTINCT oi.order_id) AS orders
FROM silver_order_items oi
JOIN silver_sellers s
  ON oi.seller_id = s.seller_id
GROUP BY
  s.seller_id,
  s.seller_city,
  s.seller_state;
