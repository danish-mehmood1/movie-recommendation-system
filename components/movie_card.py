import streamlit as st
from services.tmdb import get_movie_details
from services.youtube import get_trailer_url


def render_movie_card(movie, index):
    """
    Renders a single professional movie card.
    movie = {"movie_id": ..., "title": ..., "genres": ...}
    """

    tmdb = get_movie_details(movie["title"])
    trailer_url = get_trailer_url(movie["title"])

    st.markdown('<div class="movie-card">', unsafe_allow_html=True)

    poster_col, info_col = st.columns([1, 2])

    with poster_col:
        st.markdown('<div class="movie-poster">', unsafe_allow_html=True)
        if tmdb and tmdb.get("poster"):
            st.image(tmdb["poster"], use_container_width=True)
        else:
            st.info("Poster not available")
        st.markdown('</div>', unsafe_allow_html=True)

    with info_col:
        st.markdown(f"### {index}. 🎬 {movie['title']}")
        st.caption(f"🎭 {movie['genres']}")

        if tmdb:
            rating = float(tmdb["rating"] or 0)

            badge_class = "badge-green"
            badge_text = "Excellent"

            if rating < 8:
                badge_class = "badge-yellow"
                badge_text = "Good"

            if rating < 6:
                badge_class = "badge-red"
                badge_text = "Average"

            st.markdown(
                f'<span class="badge {badge_class}">⭐ {rating:.1f}/10 · {badge_text}</span>',
                unsafe_allow_html=True
            )

            if tmdb.get("release"):
                st.write(f"📅 **Release:** {tmdb['release']}")

            if tmdb.get("overview"):
                overview = tmdb["overview"]
                if len(overview) > 220:
                    overview = overview[:220].rstrip() + "..."
                st.write(overview)
        else:
            st.warning("Details unavailable from TMDB.")

        btn1, btn2 = st.columns(2)

        with btn1:
            st.link_button("▶️ Trailer", trailer_url, use_container_width=True)

        with btn2:
            st.button(
                "❤️ Favorite",
                key=f"fav_{movie['movie_id']}_{index}",
                disabled=True,
                help="Coming soon",
                use_container_width=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
