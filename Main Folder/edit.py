from storage import load_movies, save_movies
from m_list import list_movies


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

def main():
    movies = load_movies()
    while True:
        print("="*50)
        print("\n🎬 Movie Stocks🎬")
        print("="*50)
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Search & Sort") 
        print("6. Save and Exit")
        print("="*50)
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
            search_sort(movies) 
        elif choice == '6':
            save_movies(movies)
            print("Movies saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
