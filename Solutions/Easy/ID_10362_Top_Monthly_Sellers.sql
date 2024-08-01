WITH cte AS (SELECT
*, DENSE_RANK() OVER(PARTITION BY product_category ORDER BY total_sales DESC) AS rnk
FROM sales_data
WHERE EXTRACT(MONTH FROM sales_date) = 01) 

SELECT seller_id, total_sales, product_category, market_place, sales_date
FROM cte 
WHERE rnk <4;
