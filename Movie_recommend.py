import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset
data = {
    'Title': [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump',
        'The Lord of the Rings: The Return of the King', 'Pirates of the Caribbean: The Curse of the Black Pearl',
        'The Avengers', 'The Matrix', 'Inception',
        'Fight Club', 'The Silence of the Lambs', 'Se7en', 'The Green Mile', 'Interstellar',
        'Gladiator', 'The Lion King', 'Back to the Future', 'Jurassic Park', 'Star Wars: Episode IV - A New Hope'
    ],
    'Genre': [
        'Drama', 'Crime, Drama', 'Action, Crime, Drama', 'Crime, Drama', 'Drama, Romance',
        'Fantasy, Adventure', 'Fantasy, Adventure', 'Action, Sci-Fi', 'Sci-Fi', 'Action, Sci-Fi',
        'Drama', 'Crime, Drama, Thriller', 'Crime, Drama, Thriller', 'Crime, Drama, Fantasy', 'Adventure, Drama, Sci-Fi',
        'Action, Adventure, Drama', 'Animation, Adventure, Drama', 'Adventure, Comedy, Sci-Fi', 'Adventure, Sci-Fi, Thriller', 'Adventure, Fantasy, Sci-Fi'
    ]
}

movies_df = pd.DataFrame(data)

def capitalize_genres(genres):
    return ', '.join([genre.strip().capitalize() for genre in genres.split(',')])

movies_df['Genre'] = movies_df['Genre'].apply(capitalize_genres)

def recommend_movies(user_preferences, movies_df):
    user_preferences = capitalize_genres(user_preferences)
    user_genres = set(user_preferences.split(', '))
    
    tfidf = TfidfVectorizer(stop_words='english')
    genre_matrix = tfidf.fit_transform(movies_df['Genre'])
    user_preferences_vector = tfidf.transform([user_preferences])
    
    cosine_similarities = cosine_similarity(user_preferences_vector, genre_matrix).flatten()
    movie_indices = cosine_similarities.argsort()[::-1]
    
    recommended_movies = []
    for idx in movie_indices:
        movie_genres = set(movies_df.iloc[idx]['Genre'].split(', '))
        if user_genres & movie_genres:
            recommended_movies.append(movies_df.iloc[idx])
        if len(recommended_movies) >= 7:
            break

    if recommended_movies:
        return pd.DataFrame(recommended_movies)
    else:
        return None

# Main
user_preferences = input("Enter your preference: ")
recommended_movies_1 = recommend_movies(user_preferences, movies_df)

if recommended_movies_1 is not None:
    print("\nRecommended movies based on user preferences:\n")
    print(recommended_movies_1)
else:
    print("\nNo data found!!")
