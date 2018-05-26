#   An HTTP server fetches random movies from TMDB and displayes them allowing
#   allowing user to see artwork and watch the trailer.


from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import requests
import media
import fresh_tomatoes

# Create array for movies
movies = []

# API Key for TMDB
api_key = "ce8752a5592c63bdece91470278e20b4"


class MovieServer(BaseHTTPRequestHandler):
    """
    This class fetches movie from
    """

    #   This method fetches 20 movies from TMDB including title, storyline,
    #   artwork and Youtube URL for the trailer
    def fetch_movies():
        """
        This method fetches movies using from TMDB API using its
        discover method.

        The method iterates through the JSON result and for each movie it
        creates a Movie object including the title, storyline, artwork and
        Youtube URL for the trailer.

        The trailer URL is not available in the initial movie information so
        this is fetched using fetch_video method with movie_id
        """

        #   Make request for movies and parse response to JSON object
        request = requests.get("""https://api.themoviedb.org/3/discover/movie?
        &api_key=""" + api_key)
        response = request.json()["results"]
        counter = 0

        #   Pull relevant parameters from JSON response object story in movie
        #   object and add movie object to movies array
        for item in response:
            movie = []
            movie_id = str(response[counter]["id"])
            poster_url = ("""http://image.tmdb.org/t/p/w185/""" +
                          response[counter]["poster_path"])
            trailer_url = MovieServer.fetch_video(movie_id)
            movie = media.Movie(response[counter]["title"],
                                response[counter]["overview"],
                                poster_url,
                                trailer_url)
            movies.append(movie)
            counter = counter + 1

    #   Fetches the Youtube URL for the trailer of a given movie.
    def fetch_video(movie_id):
        """
        Fetch Youtube video key from TMDB API and returns full YouTube URL

        Paramters
        ---------
        movie_id : str
            TMDB ID of the movie for which the trailer URL is wanted.

        Returns
        -------
        trailer_url : str
            Youtube URL of trailer.
        """

        request = requests.get("""https://api.themoviedb.org/3/movie/""" +
                               movie_id + """/videos?&api_key=""" + api_key)
        response = request.json()["results"]
        youtube_key = response[0]["key"]
        trailer_url = """https://www.youtube.com/watch?v=""" + youtube_key
        return trailer_url

#   Fetch movies using method in this class and open movie page
MovieServer.fetch_movies()
fresh_tomatoes.open_movies_page(movies)





