-- We have to use the COALESCE function in this. There is no IFNULL function in PostgreSQL and NULLs are not counted in the COUNT() function for a specific column

SELECT
user_id, COALESCE(COUNT(DISTINCT activity_type),0) AS total_unique_activities
FROM user_profiles
LEFT JOIN activity_log USING(user_id)
GROUP BY 1;
