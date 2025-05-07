-- PostgreSQL Solution
SELECT
year_patron_registered, home_library_definition, MAX(total_checkouts) AS max_total_checkouts
FROM library_usage
WHERE age_range = '65 to 74 years' AND year_patron_registered = 2015 AND circulation_active_month = 'April'
GROUP BY 1,2
ORDER BY 3 DESC;
