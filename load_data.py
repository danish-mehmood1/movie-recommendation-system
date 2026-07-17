from dotenv import load_dotenv
import os
import pandas as pd
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# MySQL se connect karo
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)
cursor = conn.cursor()

# CSV files padho
movies_df = pd.read_csv("data/movies.csv")
ratings_df = pd.read_csv("data/ratings.csv")

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