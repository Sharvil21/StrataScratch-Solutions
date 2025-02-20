SELECT
EXTRACT(DAY FROM post_date) AS day, COUNT(*) AS number_of_posts
FROM facebook_posts
GROUP BY 1;
