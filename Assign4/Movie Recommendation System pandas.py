def get_top_movies_by_genre(csv_file, genre, top_n=5):
"""
Movie Recommendation System
--------------------------
This script reads a CSV file containing a list of movies and allows the user to get the top N movies by rating for a specified genre.

- The CSV file should be named 'movies.csv' and located in the same folder as this script.
- The user is prompted to enter a genre, and the script displays the top movies in that genre based on their ratings.
"""

import pandas as pd

def get_top_movies_by_genre(csv_file, genre, top_n=5):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    # Filter by genre (case-insensitive)
    filtered = df[df['genre'].str.strip().str.lower() == genre.strip().lower()]
    # Drop rows with missing or invalid ratings
    filtered = filtered.dropna(subset=['rating'])
    try:
        filtered['rating'] = filtered['rating'].astype(float)
    except ValueError:
        filtered = filtered[pd.to_numeric(filtered['rating'], errors='coerce').notnull()]
        filtered['rating'] = filtered['rating'].astype(float)
    # Sort by rating descending
    filtered = filtered.sort_values(by='rating', ascending=False)
    # Convert to list of dictionaries
    movies = filtered[['title', 'rating']].to_dict(orient='records')
    return movies[:top_n]

if __name__ == "__main__":
    # Set the CSV file path (should be in the same folder as this script)
    csv_file = "movies.csv"  # Default to the movies.csv file in the current folder
    # Prompt the user to enter a genre
    genre = input("Enter a genre (e.g., 'Action'): ")
    # Get the top movies for the specified genre
    top_movies = get_top_movies_by_genre(csv_file, genre)
    # Display the results
    if not top_movies:
        print(f"No movies found for genre '{genre}'.")
    else:
        print(f"Top {len(top_movies)} movies in genre '{genre}':")
        for movie in top_movies:
            print(f"{movie['title']} (Rating: {movie['rating']})")
