from storage import load_movies, save_movies

def add_movie(movies):
    title = input("Enter movie title: ").strip()
    while True:
        try:
            rating = int(input("Enter rating (1-5): "))
            if 1 <= rating <= 5:
                break
            else:
                print("Rating must be between 1 and 5.")
        except ValueError:
            print("Please enter a number.")
    movies.append({"title": title, "rating": rating})
    print(f"Added '{title}' with rating {rating}.")
    save_movies(movies)

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
