import streamlit as st

from recommendation.engine import recommend_movies
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.movie_card import render_movie_card
from components.footer import render_footer
from components.explorer import render_explorer


# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Load CSS
# --------------------------------------------------
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css("assets/styles.css")


# --------------------------------------------------
# Sidebar + Hero
# --------------------------------------------------
render_sidebar()
render_hero()


# --------------------------------------------------
# Tabs
# --------------------------------------------------
tab1, tab2 = st.tabs(["🎯 Recommendations", "🔍 Explore Movies"])


# --------------------------------------------------
# Tab 1: Recommendations
# --------------------------------------------------
with tab1:

    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        user_id = st.number_input(
            "👤 Enter User ID (1–610)",
            min_value=1,
            max_value=610,
            value=1,
            step=1
        )

    with col2:
        st.metric("Engine", "Collaborative Filtering")

    with col3:
        st.metric("Status", "🟢 Online")

    recommend_clicked = st.button("🎬 Recommend Movies", use_container_width=True)

    st.divider()

    if recommend_clicked:

        try:
            with st.spinner("Finding movies for you..."):
                recommendations = recommend_movies(user_id)

            if recommendations:
                st.success(f"Found {len(recommendations)} recommendations!")
                st.subheader("🍿 Recommended For You")

                for index, movie in enumerate(recommendations, start=1):
                    render_movie_card(movie, index)

            else:
                st.warning("No recommendations found for this user.")

        except Exception as e:
            st.error(f"❌ Error: {e}")


# --------------------------------------------------
# Tab 2: Explore Movies
# --------------------------------------------------
with tab2:
    render_explorer()


# --------------------------------------------------
# Footer
# --------------------------------------------------
render_footer()