import csv
from contact import Contact


def csv_to_contact(path, encoding="latin_1"):
    contacts = []

    with open(path, encoding=encoding) as file:
        # The "csv.reader(FILE)" read a file and transforms the data to a list, with index, where each line is a
        # "object", and the separator for the indexes is the "," between the data Ex.:
        # [0]  [1]              [2]
        # 1,Guilherme,guilherme@guilherme.com.br
        # 2,Elias,elias@elias.com.br
        reader = csv.reader(file)

        for line in reader:
            # Python assigns each index to variables at the same time, without having to specify them one by one
            # id, name, email = line

            id = line[0]
            name = line[1]
            email = line[2]

            contact = Contact(id, name, email)
            contacts.append(contact)

    return contacts
