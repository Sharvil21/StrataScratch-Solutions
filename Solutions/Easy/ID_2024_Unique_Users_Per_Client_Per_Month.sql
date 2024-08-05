SELECT
client_id, EXTRACT(MONTH FROM time_id) AS month, COUNT(DISTINCT user_id) AS users_num
FROM fact_events
GROUP BY 1,2
