--PostgreSQL Solution
WITH cte AS (SELECT
user_id,
SUM(CASE WHEN EXTRACT(YEAR FROM order_date) = 2021 THEN 1 ELSE 0 END) AS purchases_in_2021,
SUM(CASE WHEN EXTRACT(YEAR FROM order_date) = 2020 THEN 1 ELSE 0 END) AS purchases_in_2020
FROM amazon_orders
GROUP BY user_id)

SELECT
user_id
FROM cte
WHERE purchases_in_2021 > 2 AND purchases_in_2020 > 2;

