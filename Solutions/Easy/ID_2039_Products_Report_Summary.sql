--First Solution
SELECT
product_category, COUNT(DISTINCT transaction_id) AS transactions, SUM(sales) AS sales
FROM wfm_transactions
JOIN wfm_products USING(product_id)
WHERE EXTRACT(YEAR FROM transaction_date) = 2017
GROUP BY 1
ORDER BY 3 DESC;

--Solution using MySQL:
SELECT
product_category, COUNT(DISTINCT transaction_id) AS transactions, SUM(sales) AS sales
FROM wfm_transactions
JOIN wfm_products
USING(product_id)
WHERE EXTRACT(YEAR FROM transaction_date) = 2017
GROUP BY 1
ORDER BY 3 DESC;
