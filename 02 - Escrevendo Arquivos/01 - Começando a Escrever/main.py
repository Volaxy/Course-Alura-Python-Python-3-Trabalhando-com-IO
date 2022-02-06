def __main__():
    # By default, the reading mode for the file is the "r" (Only Read), to set the reading mode, put the parameter
    # "mode"

    # If the mode is "w", it's delete the file and replace with other (the pointer is placed in the file start)
    # file = open("data/contacts-writing.csv", mode="w")

    # If the mode is "a", it's append the content at the end of file (the pointer is placed in the file end)
    file = open("data/contacts-writing.csv", mode="a")

    contact = "11,Carol,carol@carol.com.br\n"

    # The ".write(OBJECT)" write something in the file
    # If the file is opened in the Read Mode "r", this function throw an exception
    file.write(contact)


if __name__ == "__main__":
    __main__()
