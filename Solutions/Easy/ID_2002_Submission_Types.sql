WITH cte AS (SELECT
user_id,
SUM(CASE WHEN type ~* 'Refinance' THEN 1 ELSE 0 END) AS refiance_count,
SUM(CASE WHEN type ~* 'InSchool' THEN 1 ELSE 0 END) AS inschool_count
FROM loans
GROUP BY 1)

SELECT user_id FROM cte
WHERE refiance_count > 0 AND inschool_count > 0
