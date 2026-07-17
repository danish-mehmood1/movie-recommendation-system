import streamlit as st


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <h1>🎬 Movie Recommendation System</h1>
            <p>
                Discover your next favorite movie using Collaborative Filtering,
                trained on the MovieLens dataset and enhanced with live TMDB data.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
