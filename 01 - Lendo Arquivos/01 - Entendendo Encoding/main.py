def __main__():
    # The "open()" read a file with the specified path
    file = open("data/contacts.csv")

    # The "readlines()" read all the lines of file, by default, it's returns an array with each line is an index of the
    # array
    content = file.readlines()

    for line in content:
        print(line, end="")


if __name__ == "__main__":
    __main__()
