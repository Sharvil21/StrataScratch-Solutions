SELECT
user_id, SUM(number_of_comments) AS number_of_comments
FROM fb_comments_count
WHERE created_at BETWEEN '2020-01-11' AND '2020-02-10'
GROUP BY 1
