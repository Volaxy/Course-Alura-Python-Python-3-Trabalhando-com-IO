def __main__():
    # In the mode "a+", every function of "seek()" is undone and the pointer is placed in the file end
    file = open("data/contacts-writing.csv", mode="a+")

    # The "+" after the "w", indicate to the Python which the file will be open in both write and read mode
    # file = open("data/contacts-writing.csv", mode="w+")

    contacts = ["11,Carol,carol@carol.com.br\n",
                "12,Ana,ana@ana.com.br\n",
                "13,Taz,taz@taz.com.br\n",
                "14,Felipe,felipe@felipe.com.br\n"]

    # The Python ignore the break point, for example, the "\n"
    for contact in contacts:
        file.write(contact)

    file.flush()

    # The ".seek(NUMBER)" put the pointer in the specific NUMBER passed by parameter
    # The "NUMBER" refer to the characters of a file, and not to the line
    file.seek(0)

    file.write("13,Taz,taz@taz.com.br\n".upper())
    file.flush()
    file.seek(0)

    for line in file:
        print(line)


if __name__ == "__main__":
    __main__()
