-- Have to use DENSE_RANK Window Function along with a CTE and the CONCAT Operator '||' to get the desired output

WITH cte AS (SELECT
start_timestamp, end_timestamp, device_type, SUM(user_count) AS user_count, DENSE_RANK() OVER(PARTITION BY device_type ORDER BY SUM(user_count) DESC) AS rnk
FROM user_activity
GROUP BY 1,2,3)

SELECT user_count, start_timestamp || ' to ' || end_timestamp AS time_period, device_type 
FROM cte
WHERE rnk = 1;
