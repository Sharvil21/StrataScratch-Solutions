SELECT
COUNT(DISTINCT user_id) AS total_users
FROM rc_calls
JOIN rc_users USING(user_id)
WHERE status ~* '^paid' AND EXTRACT(MONTH FROM date) = '04' AND EXTRACT(YEAR FROM date) = '2020'
