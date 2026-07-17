import streamlit as st


def render_footer():
    st.divider()
    st.markdown(
        """
        <div style="text-align:center; color:#9ca3af; padding-top:10px;">
            <b>Movie Recommendation System</b><br>
            Built by Danish Mehmood · Python, Streamlit, MySQL, Scikit-learn, TMDB API
        </div>
        """,
        unsafe_allow_html=True
    )
