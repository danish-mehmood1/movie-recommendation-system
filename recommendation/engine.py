import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from database.connection import get_connection


# -----------------------------
# Load Data
# -----------------------------
conn = get_connection()

ratings_df = pd.read_sql("SELECT * FROM ratings", conn)
movies_df = pd.read_sql("SELECT * FROM movies", conn)

conn.close()


# -----------------------------
# User-Movie Matrix
# -----------------------------
user_movie_matrix = ratings_df.pivot_table(
    index="user_id",
    columns="movie_id",
    values="rating"
).fillna(0)


# -----------------------------
# Similarity Matrix
# -----------------------------
similarity = cosine_similarity(user_movie_matrix)

similarity_df = pd.DataFrame(
    similarity,
    index=user_movie_matrix.index,
    columns=user_movie_matrix.index
)


# -----------------------------
# Recommendation Function
# -----------------------------
def recommend_movies(user_id, num_recommendations=5):

    similar_users = (
        similarity_df[user_id]
        .sort_values(ascending=False)[1:6]
        .index
    )

    similar_users_ratings = ratings_df[
        ratings_df["user_id"].isin(similar_users)
    ]

    watched_movies = ratings_df[
        ratings_df["user_id"] == user_id
    ]["movie_id"].tolist()

    recommendations = similar_users_ratings[
        ~similar_users_ratings["movie_id"].isin(watched_movies)
    ]

    top_movies = (
        recommendations.groupby("movie_id")["rating"]
        .mean()
        .sort_values(ascending=False)
        .head(num_recommendations)
    )

    result = movies_df[
        movies_df["movie_id"].isin(top_movies.index)
    ]

    return result["title"].tolist()