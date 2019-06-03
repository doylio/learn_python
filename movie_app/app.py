import json
import os
from user import User


def menu():
    print("Welcome to the Movie Tracker 5000\n")
    filename = input("Enter your username:  ")

    # Load user or init new user
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(filename)


    user_input = get_menu_input()
    while user_input.lower() != 'q':

        if user_input.lower() == 'a':
            name = input("Enter movie title:  ")
            genre = input("Enter movie genre:  ")
            user.add_movie(name, genre)

        elif user_input.lower() == 's':
            for movie in user.movies:
                print("Title:  {name}\n"
                      "Genre:  {genre}\n"
                      "Watched:  {watched}\n\n".format(
                    name=movie.name,
                    genre=movie.genre,
                    watched=movie.watched
                ))

        elif user_input.lower() == 'w':
            movie_name = input("Enter movie title:  ")
            user.set_watched(movie_name)

        elif user_input.lower() == 'd':
            movie_name = input("Enter movie title to delete:  ")
            user.delete_movie(movie_name)

        elif user_input.lower() == 'l':
            for movie in user.watched_movies():
                print("Title:  {name}\n"
                      "Genre:  {genre}\n"
                      "Watched:  {watched}\n\n".format(
                            name=movie.name,
                            genre=movie.genre,
                            watched=movie.watched
                ))

        else:
            print("I didn't understand that command")

        user_input = get_menu_input()

    # Save file
    with open(filename, 'w') as f:
        json.dump(user.json(), f)



def get_menu_input():
    command = input("Commands:\n\n"
                    "A - Add a movie\n"
                    "S - See list of movies\n"
                    "W - Set a movie as watched\n"
                    "D - Delete a movie\n"
                    "L - See list of watched movies\n"
                    "Q - Save and quit\n")
    return command

def file_exists(filename):
    return os.path.isfile(filename)



menu()