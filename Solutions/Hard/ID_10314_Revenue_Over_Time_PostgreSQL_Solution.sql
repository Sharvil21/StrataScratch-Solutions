#PostgreSQL Solution
with cte AS (SELECT
TO_CHAR(created_at,'YYYY-MM') AS MONTH, SUM(purchase_amt) AS total_revenue
FROM amazon_purchases
WHERE purchase_amt > 0
GROUP BY 1 
ORDER BY 1)

SELECT month, AVG(total_revenue) OVER(ROWS BETWEEN 2 PRECEDING AND CURRENT ROWS) AS rolling_avg
FROM cte;
