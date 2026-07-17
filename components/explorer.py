import pandas as pd
import streamlit as st

from components.movie_card import render_movie_card


@st.cache_data
def load_movies():
    df = pd.read_csv("data/movies.csv")
    df = df.rename(columns={"movieId": "movie_id"})
    return df


def get_all_genres(df):
    genres = set()
    for genre_string in df["genres"].dropna():
        for g in genre_string.split("|"):
            if g and g != "(no genres listed)":
                genres.add(g)
    return sorted(genres)


def render_explorer():

    movies_df = load_movies()
    all_genres = get_all_genres(movies_df)

    st.subheader("🔍 Explore Movies")

    search_col, genre_col = st.columns([2, 1])

    with search_col:
        search_query = st.text_input(
            "Search by movie title",
            placeholder="e.g. Toy Story, Batman, Inception..."
        )

    with genre_col:
        selected_genres = st.multiselect(
            "Filter by genre",
            options=all_genres
        )

    filtered = movies_df.copy()

    if search_query:
        filtered = filtered[
            filtered["title"].str.contains(search_query, case=False, na=False)
        ]

    if selected_genres:
        pattern = "|".join(selected_genres)
        filtered = filtered[
            filtered["genres"].str.contains(pattern, case=False, na=False)
        ]

    st.caption(f"Showing {min(len(filtered), 12)} of {len(filtered)} matching movies")

    if filtered.empty:
        st.warning("No movies match your search. Try a different title or genre.")
        return

    results = filtered.head(12).to_dict("records")

    for index, movie in enumerate(results, start=1):
        render_movie_card(movie, index)