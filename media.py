#   Class to contain movie objects including title, storyline, poster artwork
#   and Youtube trailer.

import webbrowser


class Movie():
    """ Movie class containing movie parameters and related methods. """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Constructor method which constructs Movie class using title, storyline
        poster image and Youtube trailer URL.

        Parameters
        ----------
        movie_title : str
            Title of movie

        movie_storyline : str
            Short description of movie plot.

        poster_image : byte
            Image object for poster artwork.

        trailer_youtube : str
            URL for trailer.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Method to open page and play movie trailer"""
        webbrowser.open(self.trailer_youtube_url)
