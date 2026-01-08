CREATE OR REPLACE VIEW gold_seller_performance AS
SELECT
  oi.seller_id,
  SUM(oi.price) AS sales,
  COUNT(DISTINCT oi.order_id) AS orders
FROM order_items oi
GROUP BY oi.seller_id;
