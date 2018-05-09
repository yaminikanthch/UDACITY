'''Defines the Movie class that contains the details of a movie.'''
import webbrowser


class Movie():

    '''This class provides a way to store movie related information.
Attributes:
Title: Title of the movie.
Storyline: A string to store the basic plot of the movie.
Poster_image_url: A string to store the URL of the movie poster.
Trailer_youtube_url: A string to store the URL of the movie trailer.'''
    def __init__(
        self,
        movie_title,
        movie_storyline,
        movie_poster_image,
            movie_trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    def show_trailer(self):
        '''Plays the movie trailer in the web browser.'''
        webbrowser.open(self.youtube_trailer)

