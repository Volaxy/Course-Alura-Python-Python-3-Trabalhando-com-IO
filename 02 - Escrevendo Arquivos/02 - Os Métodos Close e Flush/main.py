def __main__():
    file = open("data/contacts-writing.csv", mode="w")

    contacts = ["11,Carol,carol@carol.com.br\n",
                "12,Ana,ana@ana.com.br\n",
                "13,Taz,taz@taz.com.br\n",
                "14,Felipe,felipe@felipe.com.br\n"]

    for contact in contacts:
        file.write(contact)

    # The Python only writes in the file if the program is no longer using the file

    # The ".flush()" forces the Python to write in the file without close it
    file.flush()

    # The ".close()" close the file to indicate which the program is no longer using the file

    # file.close()

    input("Press <ENTER> to finish the program")


if __name__ == "__main__":
    __main__()
