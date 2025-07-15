# NextInRoll — because movie nights deserve better picks.

## Movie Recommendation System

This is a content-based movie recommendation system built using scikit-learn and TMDB movie metadata. It recommends similar movies based on features like title, genres, cast, and director. Additionally, it fetches movie posters using the OMDB API for a visually rich interface.

## Features

- Recommends top similar movies using cosine similarity.
- Based on movie metadata: title, genres, cast, director.
- Cleaned and preprocessed with NLTK and pandas.
- Movie posters fetched in real-time using OMDB API.
- Built with an interactive interface using Streamlit.

## How It Works

1. Load and preprocess movie data from TMDB dataset.
2. Combine relevant metadata into a single string.
3. Apply NLP techniques (e.g., stemming) to normalize text.
4. Convert metadata into numerical vectors using `CountVectorizer`.
5. Compute cosine similarity matrix for all movies.
6. When a user selects a movie, recommend the top similar ones.
7. Use OMDB API to retrieve movie posters for display.

## Tech Stack

| Task                      | Library/Tool       |
|---------------------------|--------------------|
| Data Cleaning             | `pandas`           |
| Text Preprocessing        | `nltk` (PorterStemmer) |
| Vectorization & Modeling  | `scikit-learn`     |
| Similarity Measurement    | `cosine_similarity` from `sklearn.metrics.pairwise` |
| Model Serialization       | `pickle` (`.pkl` files) |
| Poster Retrieval          | `OMDB API` via `requests` |
| User Interface            | `streamlit`        |

## Project Structure

```
MovieRecommender/
├── app.py                     # Streamlit UI application
├── utils/                     # Core logic and utility functions
│   ├── fetch.py               # OMDB poster fetch logic
│   └── engine.py              # Recommendation engine and similarity logic
├── data/                      # Raw datasets and serialized files
│   ├── tmdb_5000_movies.csv   # Shared TMDB movie metadata
│   ├── tmdb_5000_credits.csv  # Shared TMDB credits data
│   ├── similarity.pkl         # Precomputed similarity matrix (ignored in Git)
│   └── movies.pkl             # Processed movie dataframe (ignored in Git)
├── notebooks/                 # Jupyter notebooks for training / experimentation
│   └── rec.ipynb              # Model building, vectorization, and similarity calc
├── assets/                    # UI screenshots or demo images
│   
├── .gitignore                 # Excludes .pkl files and cache directories
├── requirements.txt           # List of required Python libraries
├── LICENSE                    # MIT License for reuse and distribution
└── README.md                  # Project documentation and usage guide
```


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/makwana-jaydeep/NextInRoll.git
cd MovieRecommender
```


### 2. Install Dependencies

Make sure Python 3.8+ is installed, then run:


```pip install -r requirements.txt```

### 3. Set Your OMDB API Key
In fetch.py, replace:

```omdb_api_key = ""  # Add your OMDB API key here```

You can obtain a free API key from http://www.omdbapi.com/apikey.aspx.

### 4. Run the App

```streamlit run app.py ```

The app will open in your browser at http://localhost:8501.

## Screenshots
Screenshots of the UI and recommendations can be placed in the assets/ directory.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- TMDB for the original movie dataset.

- OMDB API for poster and metadata retrieval.

- NLTK for natural language processing.

- scikit-learn for modeling and similarity computation.


