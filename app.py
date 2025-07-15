import streamlit as st
from utils.engine import load_data, recommend

st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("Movie Recommendation System")

# Load Data
movies, similarity = load_data("data/similarity.pkl", "data/movies.pkl")
movie_titles = movies['title'].values

selected_movie = st.selectbox('Choose a movie to get recommendations:', movie_titles)
omdb_api_key = ""  #  Add your OMDB API key

if st.button("Recommend"):
    names, posters = recommend(selected_movie, movies, similarity, omdb_api_key)

    cols = st.columns(5)
    for col, name, poster in zip(cols, names[:5], posters[:5]):
        with col:
            st.text(name)
            st.image(poster)

if st.button("Reset"):
    st.experimental_rerun()
