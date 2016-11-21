import movie
import fresh_tomatoes
import json

# initialize varialbes before use
json_data = {}
movie_array = []

# open the data file, read in the json data, and get the main element
with open("movie_data.json") as data_file:
    json_data = json.load(data_file)
    movies_data = json_data['movies']

# loop through the movies data and create a new movie objet for each one
for movie_data in movies_data:
	movie_array.append(movie.Movie(movie_data['title'],
                       movie_data['description'],
                       movie_data['poster'],
                       movie_data['trailer']))


# let the fresh_tomatoes object convert all this to a web page
fresh_tomatoes.open_movies_page(movie_array)
