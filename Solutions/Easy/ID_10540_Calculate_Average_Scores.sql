SELECT
project_id, AVG(score)
FROM project_data
GROUP BY 1
HAVING COUNT(team_member_id) >1;
