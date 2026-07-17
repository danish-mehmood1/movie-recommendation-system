import streamlit as st
from recommendation.engine import recommend_movies
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎬 Movie Recommendation")

st.sidebar.markdown("---")

st.sidebar.subheader("📖 About")

st.sidebar.write(
    """
This application recommends movies using
**Collaborative Filtering**.

The recommendation engine is built with:

- 🐍 Python
- 🎨 Streamlit
- 🗄️ MySQL
- 📊 Pandas
- 🤖 Scikit-learn
"""
)

st.sidebar.markdown("---")

st.sidebar.subheader("📊 Dataset")

st.sidebar.write("""
- 🎥 Movies: **9,742**
- ⭐ Ratings: **100,836**
- 👥 Users: **610**
""")

st.sidebar.markdown("---")

st.sidebar.success("✅ Portfolio Project")

# -----------------------------
# Main Title
# -----------------------------
st.title("🎬 Movie Recommendation System")

st.markdown(
"""
### Discover Movies You'll Love

This project recommends movies based on **Collaborative Filtering** using the **MovieLens Dataset**.

It analyzes users with similar preferences and recommends movies they enjoyed.
"""
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
left, right = st.columns([2, 1])

with left:

    st.subheader("👤 Select User")

    st.write(
        "Choose a User ID between **1** and **610** to receive personalized movie recommendations."
    )

    user_id = st.number_input(
        "User ID",
        min_value=1,
        max_value=610,
        value=1,
        step=1
    )

with right:

    st.metric("Users", "610")
    st.metric("Movies", "9,742")
    st.metric("Ratings", "100,836")

st.divider()

# -----------------------------
# Recommendation Button
# -----------------------------
if st.button("🎬 Recommend Movies", use_container_width=True):

    try:

        with st.spinner("Generating recommendations..."):

            recommendations = recommend_movies(user_id)

        if recommendations:

            st.success("Recommendations generated successfully!")

            st.markdown("## 🍿 Recommended Movies")

            for i, movie in enumerate(recommendations, start=1):

                st.markdown(
                    f"""
### {i}. 🎥 {movie}
"""
                )

        else:

            st.warning("No recommendations found for this user.")

    except Exception as e:

        st.error(f"❌ {e}")

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
"""
### 🚀 Technologies Used

- Python
- Streamlit
- MySQL
- Pandas
- Scikit-learn
- Collaborative Filtering
"""
)

st.divider()

st.caption(
    "Developed by Danish Mehmood | Movie Recommendation System | 2026"
)