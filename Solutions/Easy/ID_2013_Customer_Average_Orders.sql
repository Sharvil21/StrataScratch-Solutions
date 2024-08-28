SELECT
COUNT(DISTINCT customer_id) AS total_customers, AVG(amount)
FROM postmates_orders

