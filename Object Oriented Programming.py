class Movie:
    def __init__(self, title, year, genre, director, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.rating = rating

def read_movies_from_csv(file_path):
    movies = []
    with open(file_path, 'r', encoding='utf-8') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            row = line.strip().split(',')
            movie_data = dict(zip(headers, row))
            movie = Movie(
                title=movie_data['Title'],
                year=movie_data['Year'],
                genre=movie_data['Genre'],
                director=movie_data['Director'],
                rating=movie_data['Rating']
            )
            movies.append(movie)
    return movies

# Example usage
file_path = r'C:/Users/sharo/OneDrive/Documents/Intro to informatics/imdb-movies-dataset.csv'
movies = read_movies_from_csv(file_path)
for movie in movies:
    print(f"{movie.title} ({movie.year}) - {movie.genre}, directed by {movie.director}, rating: {movie.rating}")