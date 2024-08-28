SELECT
session_type, AVG(session_end-session_start) AS duration
FROM twitch_sessions
GROUP BY 1;
