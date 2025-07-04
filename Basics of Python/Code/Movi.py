#reate a class Movie with name, rating, genre.
class Movie:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre
#Create a function filter_movies(movies, genre) that takes list of movie objects and prints only the movies of the given genre.
def filter_movies(movies, genre):
    for movie in movies:
        if movie.genre == genre:
            print(f"Movie Name: {movie.name}, Rating: {movie.rating}")
#Create a list of movie objects
l1 = [Movie("Movie1", 8.5, "Action"),
      Movie("Movie2", 7.0, "Comedy"),
      Movie("Movie3", 9.0, "Action"),
      Movie("Movie4", 6.5, "Drama"),
      Movie("Movie5", 8.0, "Comedy")]
#Call the function to filter movies of genre "Action"
filter_movies(l1, "Action")
#Call the function to filter movies of genre "Comedy"
filter_movies(l1, "Comedy")
#Call the function to filter movies of genre "Drama"
filter_movies(l1, "Drama")
#Call the function to filter movies of genre "Horror"
filter_movies(l1, "Horror")  # No output since there are no Horror movies in the list
#Call the function to filter movies of genre "Sci-Fi"
filter_movies(l1, "Sci-Fi")  # No output since there are no Sci-Fi movies in the list