from storage import load_movies, save_movies
from m_list import list_movies 
def search_movie(movies):
    if not movies:
        print("No movies to search.")
        return
    term = input("Enter part of the movie title to search: ").strip().lower()
    results = [m for m in movies if term in m["title"].lower()]
    if not results:
        print(f"No movies found containing '{term}'.")
        return
    print(f"\n🔍 Search Results for '{term}':")
    print("=" * 50)
    for idx, movie in enumerate(results, 1):
        stars = "★" * movie["rating"] + "☆" * (5 - movie["rating"])
        print(f"{idx:>2}. {movie['title']:<25} {stars}  ({movie['rating']}/5)")
    print("=" * 50)
    print()


def sort_movies(movies):
    if not movies:
        print("No movies to sort.")
        return
    print("\nSort by:")
    print("1. Name (A–Z)")
    print("2. Rating (High → Low)")
    choice = input("Choose an option: ").strip()
    if choice == '1':
        movies.sort(key=lambda m: m["title"].lower())
        print("✅ Movies sorted by name (A–Z).")
    elif choice == '2':
        movies.sort(key=lambda m: m["rating"], reverse=True)
        print("✅ Movies sorted by rating (High → Low).")
    else:
        print("Invalid sort option.")
    list_movies(movies)


def search_sort(movies):
    while True:
        print("\n🛠️  Movie Tools")
        print("1. Search Movie")
        print("2. Sort Movies")
        print("3. Back to Main Menu")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            search_movie(movies)
        elif choice == '2':
            sort_movies(movies)
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")


def main():
    movies = load_movies()
    while True:
        print("\n🎬 Movie Rating App")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Movie Tools (Search & Sort)") 
        print("6. Save and Exit")
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
