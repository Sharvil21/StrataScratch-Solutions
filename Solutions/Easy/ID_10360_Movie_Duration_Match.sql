SELECT f.flight_id, e.movie_id, e.duration AS movie_duration
FROM entertainment_catalog e
JOIN flight_schedule f ON e.duration <= f.flight_duration
WHERE flight_id = 101;
