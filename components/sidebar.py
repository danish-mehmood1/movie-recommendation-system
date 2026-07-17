import streamlit as st


def render_sidebar():
    with st.sidebar:
        st.title("🎬 Movie Recommender")
        st.markdown("---")

        st.subheader("📖 About")
        st.write(
            "Personalized movie recommendations using "
            "**Collaborative Filtering**, powered by MySQL, "
            "Scikit-learn and the TMDB API."
        )

        st.markdown("---")
        st.subheader("📊 Dataset")
        st.metric("Movies", "9,742")
        st.metric("Ratings", "100,836")
        st.metric("Users", "610")

        st.markdown("---")
        st.success("✅ Portfolio Project")
