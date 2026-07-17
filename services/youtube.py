import urllib.parse


def get_trailer_url(movie_title):
    """
    Return YouTube search URL for movie trailer.
    """

    query = f"{movie_title} Official Trailer"

    return (
        "https://www.youtube.com/results?search_query="
        + urllib.parse.quote(query)
    )