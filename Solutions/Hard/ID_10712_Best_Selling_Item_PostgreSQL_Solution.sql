--PostgreSQL Solution
-- Logic is to use Dense Rank and partition by the month and then later group by the month and description. Assign RANK in descending order then in the main query, select only those rows where the rank is 1
WITH cte1 AS (SELECT
EXTRACT(MONTH FROM invoicedate) AS month, description, SUM(unitprice * quantity) AS total_paid, DENSE_RANK() OVER(PARTITION BY EXTRACT(MONTH FROM invoicedate) ORDER BY SUM(unitprice*quantity) DESC) as rnk
FROM online_retail
GROUP BY 1,2)
SELECT
month, description, total_paid
FROM cte1 WHERE rnk = 1;
