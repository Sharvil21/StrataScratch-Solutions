--MySQL Solution
--Use WHERE clause to filter out the Financials sector, and either of the continents being Asia or Europe
SELECT
company
FROM
forbes_global_2010_2014
WHERE sector = 'Financials' AND (continent = 'Asia' OR continent = 'Europe');
