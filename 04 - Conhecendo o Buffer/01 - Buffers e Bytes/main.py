def __main__():
    file = open("data/contacts.csv")

    print(type(file.buffer))

    buffer = file.buffer
    print(buffer)

    # To transform a text in a bytes text, the string doesn't any characters with ´, and the "b" is put before the
    # string
    # bytes_text = b"This is a bytes text"
    # print(bytes_text)

    # The "bytes()" transform a string in a bytes text
    bytes_text = bytes("This is a bytes text", "latin_1")
    print(bytes_text)


if __name__ == "__main__":
    __main__()
