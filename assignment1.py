"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Movies To Watch 1.0 - by Robert Sinclair.")
    movie_list = load_file()
    menu()


def load_file():
    file = open("movies.csv", "r")  # opens file with name of "test.txt"
    movie_list = []
    for line in file:
        line = (line.strip("\n")).split(",")
        line[1] = int(line[1])
        print(str(line))
        movie_list.append(line)
    return movie_list








def menu():
        choice = ""
        print("Menu:")
        print("L - List movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        while choice not in ["Q"]:
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
                add_movie()
            elif choice == "W":
                watch_movie()
            else:
                list_movies()



def add_movie():
    def watch_movie():
        add_watched = open("movies.csv", "r+")
        add_watched.write("*")






def list_movies():
    count = -1
    movies_list = open("movies.csv", "r+")
    for line in movies_list:
        stripped_line = line.rstrip()
        count += 1
        print(str(count)+" " + stripped_line)
    movies_list.close()
    menu()

main()
