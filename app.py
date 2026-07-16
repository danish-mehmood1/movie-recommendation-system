import streamlit as st
from recommend import recommend_movies

# Page ka title aur icon set karo
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

# Heading
st.title("🎬 Movie Recommendation System")
st.write("MySQL + Python + Collaborative Filtering se bana hua project")

st.divider()

# User se input lo
st.subheader("Apna User ID daalo")
user_id = st.number_input(
    "User ID (1 se 610 tak koi bhi number)", 
    min_value=1, 
    max_value=610, 
    value=1,
    step=1
)

# Button
if st.button("🔍 Recommend Movies"):
    with st.spinner("Recommendations dhoondh rahe hain..."):
        recommendations = recommend_movies(user_id)
    
    st.success(f"User {user_id} ke liye top {len(recommendations)} movies mil gayi!")
    
    st.subheader("Tumhare liye Recommended Movies:")
    for i, movie in enumerate(recommendations, start=1):
        st.write(f"**{i}.** 🎥 {movie}")

st.divider()
st.caption("Made with MySQL, Python, Pandas & Scikit-learn")