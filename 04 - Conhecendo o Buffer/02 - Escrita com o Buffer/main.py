def __main__():
    file = open("data/contacts-writing.csv", mode="w")

    print(type(file.buffer))

    bytes_text = bytes("This is a bytes text", "latin_1")

    contact = bytes("15,Verônica,veronica@veronica.com.br\n", "latin_1")

    file.buffer.write(contact)


if __name__ == "__main__":
    __main__()
