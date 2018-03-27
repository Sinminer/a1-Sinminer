"""
Replace the contents of this module docstring with your own details.
"""

from operator import itemgetter
def main():
    print("Movies To Watch 1.0 - by Robert Sinclair.")
    movie_list = sort_list(load_file())
    display_movies(movie_list)
    menu(movie_list)


def load_file():
    file = open("movies.csv", "r")  # opens file with name of "test.txt"
    movie_list = []
    for line in file:
        line = (line.strip("\n")).split(",")
        line[1] = int(line[1])
        #print(str(line))
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
                pass
            elif choice == "A":
                add_movie(movie_list)
            elif choice == "W":
                watch_movie()
            else:
                list_movies()



def add_movie(movie_list):

    print("Title: ", end="")
    movie_title = validate_strings()
    while True:
        try:
            movie_year = int(input("Year:"))
            if movie_year <= 0:
                break
            else:
                print("Invalid input, enter a valid number")
        except ValueError:
            print("Invalid input, enter a valid number")
    print("Category: ", end="")
    movie_category = validate_strings()
    movie = [movie_title,movie_year,movie_category,"n"]
    movie_list.append(movie)
    return movie_list


def validate_strings():

    while True:
        user_input = input()
        if user_input == "":
            print("Invalid input")
        else:
            break
    return user_input



add_movie()

main()
