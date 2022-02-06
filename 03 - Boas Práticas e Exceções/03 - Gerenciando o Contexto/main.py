def __main__():
    # The "with" structure close the resource after the code is complete, saving resources
    with open("data/contacts.csv") as file:
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    __main__()
