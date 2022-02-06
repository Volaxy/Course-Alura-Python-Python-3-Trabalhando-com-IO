def __main__():
    try:
        file = open("data/contacts1-writing.csv")

        for line in file:
            print(line, end="")
            number = 1 / 0
    except FileNotFoundError:
        print("File not found")
    finally:
        file.close()


if __name__ == "__main__":
    __main__()
