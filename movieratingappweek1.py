# Movie Rating App — Week 1 Version
# Goal: Add and view movies (no file saving yet)

movies = []  # list to store movie data temporarily

def add_movie():
    title = input("Enter movie title: ")
    rating = input("Enter your rating (1–10): ")
    movies.append({"title": title, "rating": rating})
    print(f"\n✅ '{title}' added successfully!\n")

def list_movies():
    if not movies:
        print("\nNo movies added yet.\n")
        return
    print("\n🎞️ Your Movies:")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie['title']} - Rating: {movie['rating']}")
    print()

def main():
    while True:
        print("🎬 Movie Rating App")
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Edit")
        print("4. Delete Movie")
        print("5. Save and Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("\nInvalid option. Please try again.\n")

main()
