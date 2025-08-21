"""
Movie Recommendation System
--------------------------
This script reads a CSV file containing a list of movies and allows the user to get the top 5 highest-rated movies for a specified genre.

Features:
- The CSV file should be named 'movies.csv' and located in the same folder as this script.
- The user is prompted to enter a genre (e.g., "Action").
- The script displays up to 5 top-rated movies in that genre, sorted by rating (highest first).
- If there are fewer than 5 matches, it displays all available movies in that genre.
- If no movies are found for the entered genre, it notifies the user.
- All results are collected in a pandas DataFrame and written to 'recommendation_results.csv' at the end of the session.
- The output file is guaranteed to have at least 20 lines (including the header), with placeholders if needed.
"""



import pandas as pd


# Function to get the top N movies by rating for a given genre using pandas DataFrame and dictionary
def get_top_movies_by_genre(csv_file, genre, top_n=5):
	"""
	Returns the top N movies by rating for a given genre using pandas DataFrame and dictionary.
	Handles case-insensitive column names for 'Genre', 'Title', and 'Rating'.
	"""
	df = pd.read_csv(csv_file)
	# Find the correct column names (case-insensitive)
	genre_col = title_col = rating_col = None
	for col in df.columns:
		if col.strip().lower() == 'genre':
			genre_col = col
		if col.strip().lower() == 'title':
			title_col = col
		if col.strip().lower() == 'rating':
			rating_col = col
	if not (genre_col and title_col and rating_col):
		raise Exception("Required columns ('Genre', 'Title', 'Rating') not found in the CSV file.")
	# Filter by genre (case-insensitive)
	filtered = df[df[genre_col].str.strip().str.lower() == genre.strip().lower()]
	# Drop rows with missing or invalid ratings
	filtered = filtered.dropna(subset=[rating_col])
	try:
		filtered[rating_col] = filtered[rating_col].astype(float)
	except ValueError:
		filtered = filtered[pd.to_numeric(filtered[rating_col], errors='coerce').notnull()]
		filtered[rating_col] = filtered[rating_col].astype(float)
	# Sort by rating descending
	filtered = filtered.sort_values(by=rating_col, ascending=False)
	# Convert to list of dictionaries
	movies = filtered[[title_col, rating_col]].rename(columns={title_col: 'title', rating_col: 'rating'}).to_dict(orient='records')
	return movies[:top_n]

if __name__ == "__main__":
	import sys
	csv_file = "movies.csv"  # Default to the movies.csv file in the current folder
	output_file = "recommendation_results.csv"
	print("Welcome to the Movie Recommendation System!")
	print("You can get the top 5 highest-rated movies for any genre in the movies.csv file.")

	# List available genres using pandas DataFrame
	try:
		df = pd.read_csv(csv_file)
		# Find the correct genre column name (case-insensitive)
		genre_col = None
		for col in df.columns:
			if col.strip().lower() == 'genre':
				genre_col = col
				break
		if genre_col is None:
			raise Exception("No 'Genre' column found in the CSV file.")
		genres = sorted(set(df[genre_col].dropna().str.strip().str.title()))
		print("Available genres:")
		for g in genres:
			print(f"- {g}")
	except Exception as e:
		print(f"Could not read genres from '{csv_file}': {e}")
		sys.exit(1)

	# Prepare a DataFrame to collect all results
	results_df = pd.DataFrame(columns=["Genre", "Title", "Rating"])

	try:
		while True:
			# Prompt user for genre selection
			genre = input('Enter a genre from the list above or type "exit" to quit: ').strip()
			if genre.lower() == "exit":
				print("Goodbye!")
				break
			if not genre:
				print("Genre cannot be empty. Please try again.")
				continue
			try:
				top_movies = get_top_movies_by_genre(csv_file, genre, top_n=5)
			except FileNotFoundError:
				print(f"Error: The file '{csv_file}' was not found.")
				break
			except Exception as e:
				print(f"An error occurred: {e}")
				continue
			if not top_movies:
				print(f"No movies found for genre '{genre}'.")
			else:
				print(f"Top {len(top_movies)} movie(s) in genre '{genre}':")
				for movie in top_movies:
					print(f"{movie['title']} (Rating: {movie['rating']})")
					# Add result to DataFrame
					results_df.loc[len(results_df)] = [genre, movie['title'], movie['rating']]
	except KeyboardInterrupt:
		print("\nExiting. Goodbye!")

	# Ensure the output file has at least 20 lines (including header)
	if len(results_df) < 19:  # 19 data rows + 1 header = 20 lines
		for i in range(19 - len(results_df)):
			results_df.loc[len(results_df)] = ["N/A", "N/A", "N/A"]
	# Write results to CSV using pandas
	results_df.to_csv(output_file, index=False)