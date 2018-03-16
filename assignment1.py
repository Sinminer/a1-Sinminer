"""
Replace the contents of this module docstring with your own details.
"""


def main():
    print("Movies To Watch 1.0 - by Robert Sinclair.")
    load_list()

def load_list():
    movie_amount = len(open("movies.csv").readlines())
    print("{} Movies loaded".format(movie_amount))






if __name__ == '__main__':
    main()
