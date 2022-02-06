def __main__():
    file = open("data/contacts.csv")

    """
    # The "for" structure for the file read line by line to the end of file
    # This file reading structure is more performant than the "readlines()" function as it consumes less memory
    
    for line in file:
        print(line, end="")
    """

    # The "readline()" read only one line of the file
    content = file.readline()
    print(content)

    # The "readline(NUMBER)" read only the first x characters of the file
    content = file.readline(10)
    print(content)

    # Now the file pointer is on the second line as the first line has already been read by the other function
    content = file.readline()
    print(content)


if __name__ == "__main__":
    __main__()
