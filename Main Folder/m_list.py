from storage import load_movies, save_movies

def list_movies(movies):
    if not movies:
        print("No movies found.")
        return
    print("\n🎞️  Your Movies")
    print("=" * 40)
    for idx, movie in enumerate(movies, 1):
        stars = "★" * movie["rating"] + "☆" * (5 - movie["rating"])
        print(f"{idx:>2}. {movie['title']:<25} {stars}  ({movie['rating']}/5)")
    print("=" * 40)
    print()


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
