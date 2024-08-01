-- Have to use EXTRACT function for this

SELECT
week, SUM(quantity)
FROM
orders_analysis
WHERE EXTRACT(QUARTER FROM week) = 1
GROUP BY 1;
