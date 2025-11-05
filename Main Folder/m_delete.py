from storage import load_movies, save_movies
from m_list import list_movies

def delete_movie(movies):
    if not movies:
        print("No movies to delete.")
        return
    list_movies(movies)
    try:
        idx = int(input("Enter movie number to delete: ")) - 1
        if 0 <= idx < len(movies):
            confirm = input(f"Delete '{movies[idx]['title']}'? (y/n): ").lower()
            if confirm == 'y':
                removed = movies.pop(idx)
                print(f"Deleted '{removed['title']}'.")
                save_movies(movies)
            else:
                print("Deletion cancelled.")
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
