--PostgreSQL solution
--We have to use the WHERE clause to filter the required rows
SELECT
company
FROM
forbes_global_2010_2014
WHERE sector = 'Financials' AND (continent = 'Asia' OR continent = 'Europe');
