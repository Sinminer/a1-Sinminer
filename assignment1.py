"""
Replace the contents of this module docstring with your own details.
"""

from operator import itemgetter
def main():
    print("Movies To Watch 1.0 - by Robert Sinclair.")
    movie_list = sort_list(load_file())
    menu(movie_list)

"""
open file
load file into movie list
strip and spilt the list
convert row 1 of the list into a integer
once every row has been read return the movie list
"""
def load_file():
    file = open("movies.csv", "r")
    movie_list = []
    for line in file:
        line = (line.strip("\n")).split(",")
        line[1] = int(line[1])
        movie_list.append(line)
    print("{} movies loaded".format(len(movie_list)))
    return movie_list




def display_movies(movie_list):
    watched_count = 0
    for i in range(len(movie_list)):
        if movie_list[i][3] == "n":

            print("{0}. * {1[0]:<35} -  {1[1]:>4} ({1[2]})".format(i, movie_list[i]))
        else:
            watched_count += 1
            print("{0}.  {1[0]:<35} -  {1[1]:>4} ({1[2]})".format(i, movie_list[i]))
    print("{} movies watched, {} movies still to watch".format(watched_count, len(movie_list) - watched_count))
    menu(movie_list)


def sort_list(movie_list):
    return sorted(movie_list, key=(itemgetter(1, 0)))


def menu(movie_list):
        choice = ""
        print("Menu:")
        print("L - List movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        while choice != "Q":
            choice = (input(">>>")).upper()
            if choice not in ["Q","A","L","W"]:
                print("Invalid menu choice")
                print("Menu:")
                print("L - List movies")
                print("A - Add new movie")
                print("W - Watch a movie")
                print("Q - Quit")
            elif choice == "Q":
                save_movies(movie_list)
            elif choice == "A":
                add_movie(movie_list)
            elif choice == "W":
                watch_movie(movie_list)
            else:
                display_movies(movie_list)

def add_movie(movie_list):
    print("Title: ", end="")
    movie_title = validate_strings()
    while True:
        try:
            movie_year = int(input("Year:"))
            if movie_year >= 0:
                break
            else:
                print("Invalid input, enter a valid number")
        except ValueError:
            print("Invalid input, enter a valid number")
    print("Category: ", end="")
    movie_category = validate_strings()
    movie = [movie_title,movie_year,movie_category, "n"]
    movie_list.append(movie)
    return movie_list

def validate_strings():
    while True:
        user_input = input()
        if user_input == "":
            print("Input can not be blank")
        else:
            break
    return user_input
"""
ask user for the movie they want to watch
check if the number is valid and not watched
if number is valid remove the unwatched symbol and change it to watched
if not a valid number ask the user for the correct input
once complete return updated movie_list
"""
def watch_movie(movie_list):
    while True:
        try:
            movie_index = int(input("Enter the number of a movie to mark as watched:"))
            if movie_index <= -1:
                print("Number must be >= -1")
            else:
                if movie_list[movie_index][3] == "y":
                    print("Invalid movie number")
                else:
                    movie_list[movie_index][3]= "y"
                    display_movies(movie_list)
                    break
        except ValueError:
            print("Enter a valid number")
    return movie_list

def save_movies(movie_list):
    closing_file = open("movies.csv", 'w')
    for i in range(0,len(movie_list)):
        closing_file.write("{0[0]},{0[1]},{0[2]},{0[3]}\n".format(movie_list[i]))
    closing_file.close()
    print("{} moves saved to {}".format(len(movie_list), "movies.csv"))

main()
