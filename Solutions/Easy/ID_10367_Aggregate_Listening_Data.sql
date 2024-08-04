SELECT
user_id, ROUND(SUM(listen_duration)/60) AS total_listen_duration, COUNT(DISTINCT song_id) AS unique_song_count
FROM listening_habits
GROUP BY 1;
