
# An HTTP server fetches random movies from TMDB and displayes them allowing
# allowing user to see artwork and watch the trailer.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import requests
import media
import fresh_tomatoes

# Create array for movies
movies = []

#keyword = "action"

# API Key for TMDB
api_key ="ce8752a5592c63bdece91470278e20b4"


class MovieServer(BaseHTTPRequestHandler):

    #Fetch 20 movies from TMDB
    def fetch_movies():

        #Make request for movies and parse response to JSON object
        request = requests.get("""https://api.themoviedb.org/3/discover/movie?&api_key=""" + api_key)
        response = request.json()["results"]
        counter = 0
        
        #Pull relevant parameters from JSON response object story in movie object
        # and add movie object to movies array
        for item in response:
            movie = []
            movie_id = str(response[counter]["id"])
            poster_url = """http://image.tmdb.org/t/p/w185/""" + response[counter]["poster_path"]
            trailer_url = MovieServer.fetch_video(movie_id)
            movie = media.Movie(response[counter]["title"],
                        response[counter]["overview"],
                        poster_url,
                        trailer_url)
            movies.append(movie)
            counter=counter+1


    #Fetch Youtube video key from TMDB and return full YouTube URL
    def fetch_video(movie_id):
        request = requests.get("""https://api.themoviedb.org/3/movie/""" + movie_id +"""/videos?&api_key=""" + api_key)
        response = request.json()["results"]
        youtube_key = response[0]["key"]
        trailer_url = """https://www.youtube.com/watch?v=""" + youtube_key
        return trailer_url

#Fetch movies using this class and open movie page       
MovieServer.fetch_movies()
fresh_tomatoes.open_movies_page(movies)



