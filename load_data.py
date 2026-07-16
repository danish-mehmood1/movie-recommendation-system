import pandas as pd
import mysql.connector

# MySQL se connect karo
conn = mysql.connector.connect(
    host="localhost",
    user="root",           # tumhara MySQL username
    password="Password",  # apna actual password daalo
    database="movie_recommender"
)
cursor = conn.cursor()

# CSV files padho
movies_df = pd.read_csv("movies.csv")
ratings_df = pd.read_csv("ratings.csv")

# Movies table mein data daalo
for i, row in movies_df.iterrows():
    cursor.execute(
        "INSERT INTO movies (movie_id, title, genres) VALUES (%s, %s, %s)",
        (row['movieId'], row['title'], row['genres'])
    )

# Ratings table mein data daalo
for i, row in ratings_df.iterrows():
    cursor.execute(
        "INSERT INTO ratings (user_id, movie_id, rating, timestamp) VALUES (%s, %s, %s, %s)",
        (row['userId'], row['movieId'], row['rating'], row['timestamp'])
    )

conn.commit()  # changes save karo
print("Data successfully loaded!")

cursor.close()
conn.close()