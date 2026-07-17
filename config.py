import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

APP_NAME = "Movie Recommendation System"
APP_VERSION = "1.0.0"