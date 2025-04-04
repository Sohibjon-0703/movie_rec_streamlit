import pandas as pd
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sns.set()

class MovieRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
        self.data.drop(columns=['certificate', 'box_office', 'budget'], inplace=True)
        self.data['joint_string'] = self.data.apply(self.convert_into_large_string, axis=1)
        self.tfidf = TfidfVectorizer(max_features=2000)
        self.matrix = self.tfidf.fit_transform(self.data['joint_string'])
        self.ratings = {}

        # joining the columns which will be used to recommend movies

    def convert_into_large_string(self, row):
        genres = " ".join(item.strip().replace(" ", "") for item in row["genre"].split(","))
        casts = " ".join(item.strip().replace(" ", "") for item in row["casts"].split(","))
        directors = " ".join(item.strip().replace(" ", "") for item in row["directors"].split(","))
        writers = " ".join(item.strip().replace(" ", "") for item in row["writers"].split(","))
        return f"{genres} {casts} {directors} {writers}"


    # getting all genres for a selectbox in UI

    def get_unique_genres(self):
        genres = set()
        for genre_list in self.data['genre'].dropna():
            for genre in genre_list.split(','):
                genres.add(genre.strip())
        return sorted(genres)

    def recommend(self, input_genre, input_casts, input_directors, top_n=5):
        user_input = f"{input_genre} {input_casts} {input_directors}"
        user_input_matrix = self.tfidf.transform([user_input])
        similarity_scores = cosine_similarity(user_input_matrix, self.matrix)
        similar_indices = similarity_scores.argsort()[0][-top_n-1:-1][::-1]

        recommendations = self.data.iloc[similar_indices][['name', 'year', 'rating', 'genre', 'casts', 'directors']]
        recommendations['similarity'] = similarity_scores[0][similar_indices]

        return recommendations.reset_index(drop=True)
