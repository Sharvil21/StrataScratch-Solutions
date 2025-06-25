--PostgreSQL Solution
--Join the two tables first on post_id
--Use the WHERE clause to filter out the condition where reaction = 'heart'
--Then SELECT DISTINCT a.* for the result
SELECT
DISTINCT a.*
FROM facebook_posts a
JOIN facebook_reactions b
ON a.post_id = b.post_id
WHERE b.reaction ~* 'heart';
