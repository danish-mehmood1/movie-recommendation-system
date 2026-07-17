import re
import requests
from config import TMDB_API_KEY

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def get_movie_details(movie_title):
    """
    Search movie on TMDB and return
    poster, rating, release date and overview.
    """

    # Remove year from MovieLens titles
    movie_title = re.sub(r"\(\d{4}\)", "", movie_title).strip()

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_title
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if not data.get("results"):
            return None

        movie = data["results"][0]

        poster = None
        if movie.get("poster_path"):
            poster = IMAGE_URL + movie["poster_path"]

        return {
            "title": movie.get("title"),
            "poster": poster,
            "rating": movie.get("vote_average"),
            "release": movie.get("release_date"),
            "overview": movie.get("overview")
        }

    except Exception:
        return None