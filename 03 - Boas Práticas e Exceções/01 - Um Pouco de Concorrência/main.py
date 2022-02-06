def __main__():
    """"
    file1 = open("data/contacts-writing.csv", mode="w")
    file2 = open("data/contacts-writing.csv", mode="w")

    contact1 = "11,Carol,carol@carol.com.br\n"
    contact2 = "12,Andres,andres@andres.com.br\n"

    file1.write(contact1)
    file2.write(contact2)

    # Good practice is to always close the files that will no longer be used to avoid the concurrency problem
    file1.close()
    file2.close()
    """

    # The "try finally" structure, tries to perform the operations inside the "try", and regardless of whether it gives
    # an error or not, it executes what is in the "finally" block
    try:
        file = open("data/contacts-writing.csv")

        for line in file:
            print(line, end="")
            number = 1 / 0
    finally:
        file.close()


if __name__ == "__main__":
    __main__()
