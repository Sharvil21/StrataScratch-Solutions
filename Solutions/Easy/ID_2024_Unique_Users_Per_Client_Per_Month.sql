--First attempt
SELECT
client_id, EXTRACT(MONTH FROM time_id) AS month, COUNT(DISTINCT user_id) AS users_num
FROM fact_events
GROUP BY 1,2

--Second attempt using PostgreSQL
SELECT
client_id, EXTRACT(MONTH FROM time_id) AS month, COUNT(DISTINCT user_id) AS users
FROM fact_events
GROUP BY 1,2

--Solution using MySQL
SELECT
client_id, MONTH(time_id) AS 'month', COUNT(DISTINCT user_id) AS users_num
FROM fact_events
GROUP BY 1,2;

