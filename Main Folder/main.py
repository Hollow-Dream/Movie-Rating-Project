from storage import load_movies, save_movies
from add import add_movie
from m_list import list_movies
from edit import edit_movie
from m_delete import delete_movie

#We pull functions from all the different py files to run the entire app in one file, the main.py file. 
#We do this to both organize and make the code clean and readable


#This function, def main, serves as the main menu for the app. It also uses every other function from all the other files to run.

def main():
    movies = load_movies()
    while True:
        print("=" * 40)
        print("\n🎬\t Movie Rating App")
        print("=" * 50)
        print("1.\t\t Add Movie")
        print("2.\t\t View Movies")
        print("3.\t\t Edit Movie")
        print("4.\t\t Delete Movie")
        print("5.\t\t Save and Exit")
        print("=" * 50)
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



