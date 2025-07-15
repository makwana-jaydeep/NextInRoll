import pandas as pd
import pickle as pk
from utils.fetch import fetch_poster

def load_data(similarity_path: str, movies_path: str):
    with open(similarity_path, 'rb') as f:
        similarity = pk.load(f)

    with open(movies_path, 'rb') as f:
        db = pk.load(f)

    return pd.DataFrame(db), similarity


def recommend(movie: str, movies: pd.DataFrame, similarity, omdb_api_key: str):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:9]

    recommended = []
    posters = []

    for i in movie_indices:
        title = movies.iloc[i[0]].title
        recommended.append(title)
        posters.append(fetch_poster(title, omdb_api_key))

    return recommended, posters

if __name__ == '__main__':
    print("engine working..")