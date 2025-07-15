import requests

def fetch_poster(movie_title: str, omdb_api_key: str) -> str:
    omdb_url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&t={movie_title}"
    response = requests.get(omdb_url)
    data = response.json()

    return data.get("Poster", "")

if __name__ == "__main__":
    print("poster fetching..")