import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_secret(key):
    try:
        return st.secrets[key]
    except:
        return os.getenv(key)

DB_CONFIG = {
    "host": get_secret("DB_HOST"),
    "port": int(get_secret("DB_PORT")),
    "user": get_secret("DB_USER"),
    "password": get_secret("DB_PASSWORD"),
    "database": get_secret("DB_NAME")
}

TMDB_API_KEY = get_secret("TMDB_API_KEY")

APP_NAME = "Movie Recommendation System"
APP_VERSION = "1.0.0"