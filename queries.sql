-- ================================
-- Movie Recommendation System - SQL Queries
-- ================================

-- Query 1: Top 10 highest rated movies (minimum 50 ratings)
SELECT m.title, AVG(r.rating) AS avg_rating, COUNT(r.rating) AS num_ratings
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.title
HAVING num_ratings >= 50
ORDER BY avg_rating DESC
LIMIT 10;

-- Query 2: Most popular genre by number of ratings
SELECT genres, COUNT(*) AS total_ratings
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY genres
ORDER BY total_ratings DESC
LIMIT 5;

-- Query 3: Total number of unique users and movies
SELECT COUNT(DISTINCT user_id) AS total_users FROM ratings;
SELECT COUNT(*) AS total_movies FROM movies;