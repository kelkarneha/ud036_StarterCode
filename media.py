import webbrowser


class Movie():
    """The class movie defines our movie object"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """__init__ initializes the movie object and """
        """ creates  space for it in memory"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """show_trailer method opens browser window and """
        """starts playing the movie trailer from youtube"""
        webbrowser.open(self.trailer_youtube_url)

    
