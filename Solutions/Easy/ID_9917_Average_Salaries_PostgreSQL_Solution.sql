--PostgreSQL Solution
--Have to use a window function here along with an aggregate function to get the column that shows the average salary for each department beside the salary of each employee
SELECT
department, first_name, salary, AVG(salary) OVER(PARTITION BY department) AS avg_salary
FROM employee; 
