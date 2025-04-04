import streamlit as st
import pandas as pd
from recommender import MovieRecommender
import altair as alt

st.set_page_config(page_title="AI Movie Recommender", layout="wide")

# Loading the data
@st.cache_resource
def load_recommender():
    return MovieRecommender("data/IMDB Top 250 Movies.csv")

recommender = load_recommender()
all_genres = recommender.get_unique_genres()

# Initialize session state
if "ratings" not in st.session_state:
    st.session_state.ratings = {}
if "recommendations" not in st.session_state:
    st.session_state.recommendations = pd.DataFrame()

# Page Title
st.title("🎬 AI Movie Recommendation System")
st.write("Get personalized movie suggestions based on your favorite genres, actors, and directors.")

# Sidebar Inputs
st.sidebar.header("Your Preferences")

# multiselect for genres

selected_genres = st.sidebar.multiselect("🎭 Select Genres", all_genres, default=["Adventure", "Crime"])
input_genres = ", ".join(selected_genres)

input_casts = st.sidebar.text_input("⭐ Favorite Actors (comma-separated)", "Christian Bale, Heath Ledger")
input_directors = st.sidebar.text_input("🎬 Favorite Directors (comma-separated)", "Christopher Nolan")


if st.sidebar.button("Get Recommendations"):
    with st.spinner("Finding the best matches for you..."):
        recommendations = recommender.recommend(input_genres, input_casts, input_directors)
        st.session_state.recommendations = recommendations
        if recommendations.empty:
            st.warning("No recommendations found. Try different inputs.")
        else:
            st.success("Here are some movies you might enjoy:")

if not st.session_state.recommendations.empty:
    for idx, row in st.session_state.recommendations.iterrows():
        st.markdown(f"### 🎥 {row['name']} ({row['year']})")
        st.markdown(f"**Genre**: {row['genre']}  \n"
                    f"**Director**: {row['directors']}  \n"
                    f"**Cast**: {row['casts']}  \n"
                    f"**IMDB Rating**: {row['rating']} ⭐  \n"
                    f"**Similarity Score**: `{row['similarity']:.2f}`")

        # Add user rating selectbox (0–5)
        user_rating = st.selectbox(
            f"Your rating for '{row['name']}'",
            options=[0, 1, 2, 3, 4, 5],
            index=0,
            key=f"user_rating_{row['name']}"
        )
        if user_rating > 0:
            st.session_state.ratings[row['name']] = user_rating


if st.session_state.ratings:
    st.markdown("---")
    st.subheader("⭐ Your Ratings Summary")
    ratings_df = pd.DataFrame(list(st.session_state.ratings.items()), columns=["Movie", "Rating"])
    st.dataframe(ratings_df)

    st.subheader("📊 Ratings Chart")
    chart = alt.Chart(ratings_df).mark_bar().encode(
        x=alt.X("Movie:N", sort="-y"),
        y="Rating:Q",
        tooltip=["Movie", "Rating"]
    ).properties(height=400).interactive()
    st.altair_chart(chart, use_container_width=True)
