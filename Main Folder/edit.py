from storage import load_movies, save_movies
from m_list import list_movies


#This file is made for editing movies, save movies is used so that after you edit a movie it saves automatically.
#If there are no movies to edit it returns you to the main menu
#If there are movies, it asks you to enter the movie number so that you can edit
#Afterwards you are able to edit the name and the rating

def edit_movie(movies):
    if not movies:
        print("No movies to edit.")
        return
    list_movies(movies)
    try:
        idx = int(input("Enter movie number to edit: ")) - 1
        if 0 <= idx < len(movies):
            new_title = input(f"New title (leave blank to keep '{movies[idx]['title']}'): ").strip()
            if new_title:
                movies[idx]['title'] = new_title
            while True:
                new_rating = input(f"New rating (1-5, leave blank to keep {movies[idx]['rating']}): ").strip()
                if not new_rating:
                    break
                try:
                    new_rating = int(new_rating)
                    if 1 <= new_rating <= 5:
                        movies[idx]['rating'] = new_rating
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Please enter a number.")
            print("Movie updated.")
            save_movies(movies)
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Please enter a valid number.")


#Def main added for debugging, and testing purposes.

def main():
    movies = load_movies()
    while True:
        print("\n🎬 Movie Rating App")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Save and Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            list_movies(movies)
        elif choice == '3':
            edit_movie(movies)
        elif choice == '4':
            delete_movie(movies)
        elif choice == '5':
            save_movies(movies)
            print("Movies saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
