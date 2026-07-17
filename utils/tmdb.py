import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")

BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def get_movie_poster(tmdb_id):
    """
    Returns poster URL using TMDB movie ID.
    """

    if not tmdb_id:
        return None

    url = f"https://api.themoviedb.org/3/movie/{int(tmdb_id)}?api_key={API_KEY}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        poster_path = data.get("poster_path")

        if not poster_path:
            return None

        return BASE_IMAGE_URL + poster_path

    except Exception:
        return None