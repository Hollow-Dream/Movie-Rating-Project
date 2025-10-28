import json
import os

FILENAME = "movies.json"

def load_movies():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_movies(movies):
    with open(FILENAME, "w") as f:
        json.dump(movies, f, indent=2)
