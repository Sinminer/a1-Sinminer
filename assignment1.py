"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Movies To Watch 1.0 - by Robert Sinclair.")
    load_list()
    menu()


def load_list():
    movie_amount = len(open("movies.csv").readlines())
    print("{} Movies loaded".format(movie_amount))


def menu():
        choice = ""
        print("Menu:")
        print("L - List movies")
        print("A - Add new movie")
        print("W - Watch a a movie")
        print("Q - Quit")
        while choice not in ["Q","A","L","W"]:
            choice = (input(">>>")).upper()
            if choice not in ["Q","A","L","W"]:
                print("Invalid menu choice")
                print("Menu:")
                print("L - List movies")
                print("A - Add new movie")
                print("W - Watch a a movie")
                print("Q - Quit")
            else:
                pass













if __name__ == '__main__':
    main()
