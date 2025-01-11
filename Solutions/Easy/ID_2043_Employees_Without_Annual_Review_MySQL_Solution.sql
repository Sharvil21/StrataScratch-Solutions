--First MySQL Solution
WITH cte AS (SELECT
a.first_name, a.id, COUNT(b.review_date) AS total_reviews
FROM uber_employees a
LEFT JOIN uber_annual_review b
ON a.id = b.emp_id
GROUP BY 1,2
HAVING COUNT(b.review_date) = 0)

SELECT 
first_name, last_name, hire_date, termination_date
FROM uber_employees
WHERE id IN (SELECT id FROM cte)
ORDER BY hire_date DESC;

--Second MySQL Solution
SELECT
first_name, last_name, hire_date, termination_date
FROM uber_employees
WHERE id NOT IN (SELECT DISTINCT emp_id FROM uber_annual_review)
ORDER BY 3 DESC;
