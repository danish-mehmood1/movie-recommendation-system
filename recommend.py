import pandas as pd
import mysql.connector
from sklearn.metrics.pairwise import cosine_similarity

# MySQL se connect karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password",   # apna actual password daalo
    database="movie_recommender"
)

# Data ko MySQL se seedha pandas mein le aao
ratings_df = pd.read_sql("SELECT * FROM ratings", conn)
movies_df = pd.read_sql("SELECT * FROM movies", conn)

conn.close()  # connection band kar do, ab zaroorat nahi

# ---- Matrix banao: rows = users, columns = movies, values = ratings ----
user_movie_matrix = ratings_df.pivot_table(
    index='user_id', 
    columns='movie_id', 
    values='rating'
).fillna(0)

# ---- Har user ka doosre users ke saath similarity nikalo ----
similarity = cosine_similarity(user_movie_matrix)
similarity_df = pd.DataFrame(
    similarity, 
    index=user_movie_matrix.index, 
    columns=user_movie_matrix.index
)

# ---- Recommendation function ----
def recommend_movies(user_id, num_recommendations=5):
    # Is user ke sabse similar 5 users dhundo (khud ko chhod ke)
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:6].index

    # Un similar users ne jo ratings di hain, wo nikalo
    similar_users_ratings = ratings_df[ratings_df['user_id'].isin(similar_users)]

    # Jo movies apna user pehle hi dekh chuka hai, unhe hata do
    watched = ratings_df[ratings_df['user_id'] == user_id]['movie_id'].tolist()
    recommendations = similar_users_ratings[~similar_users_ratings['movie_id'].isin(watched)]

    # In movies ka average rating nikal ke top wali select karo
    top_movies = (
        recommendations.groupby('movie_id')['rating']
        .mean()
        .sort_values(ascending=False)
        .head(num_recommendations)
    )

    # Movie IDs se actual titles nikalo
    result = movies_df[movies_df['movie_id'].isin(top_movies.index)]
    return result['title'].tolist()


# ---- Test karo ----
if __name__ == "__main__":
    user_id = 1
    print(f"User {user_id} ke liye recommended movies:\n")
    for movie in recommend_movies(user_id):
        print(f"🎥 {movie}")