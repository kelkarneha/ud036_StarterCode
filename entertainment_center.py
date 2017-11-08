# This file will open a browser window which will show posters of all the
# movies defined here. Clicking on a movie poster will start playing
# the movie trailer


# media.py contains the class definiton for the movie class
import media

# fresh_tomatoes contains all the code required for creating the webpage
# displaying the movie posters and trailers
import fresh_tomatoes

# Movies are defined here
# Alternatively we can get movie data from IMDB using API
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/"
                     "Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Put all favorite movies in a single arry which is passed as argument to
# open_movies_page function
movies = [toy_story, avatar]

# open_movies_page function defines in fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)

