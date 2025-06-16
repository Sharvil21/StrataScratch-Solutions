#PostgreSQL Solution
SELECT
TO_CHAR(created_at,'YYYY-MM') AS MONTH, SUM(purchase_amt) AS total_revenue
FROM amazon_purchases
WHERE purchase_amt > 0
GROUP BY 1 
ORDER BY 1
