# Movie Server

This server fetches 20 random movies from The Movie DB using its API.  Movie classes are created for each movie, including parameters such as title, storyline, poster artwork and trailer URL.

Subseqeuntly a webpage will be served showing the posters of each movie. When a poster is clicked another window will open where the respective trailer will be played.


## How to use
The server is written in Python 3.6.5, so Python 3 shall be downloaded and used to run the file movie_server.py

1. Clone the directory
2. Navigate to the directory cd repository_name
3. If needed download Python 3 (version 3.6.5 is recommended)
4. IDLE: Open IDLE
3. Run the program with the command python3 movie_server.py
5. In the menu bar click on Run -> Run Module or press F5 on your keyboard

## Troubleshooting
If the error "no module named http.server" is received, it is likely Python 2.x is being run.  Please upgrade to Python 3.6.5 here:
https://www.python.org/downloads/ 

If code needs porting from Python 2 to 3 help can be found here:
https://docs.python.org/3/howto/pyporting.html
