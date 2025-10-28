import json
import os

#this is the name of the json file that will save all of the movie data
FILENAME = "movies.json"

#This function load_movies, is used to load data from the movies.json file, so that you can always have your movies.
def load_movies():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

#This function save_movies is used to save any movies once you add a movie and also once you exit the program.
def save_movies(movies):
    with open(FILENAME, "w") as f:
        json.dump(movies, f, indent=2)

