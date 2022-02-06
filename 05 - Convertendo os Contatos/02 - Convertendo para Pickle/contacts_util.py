import csv
import pickle

from contact import Contact


def csv_to_contact(path, encoding="latin_1"):
    contacts = []

    with open(path, encoding=encoding) as file:
        reader = csv.reader(file)

        for line in reader:
            id, name, email = line

            contact = Contact(id, name, email)
            contacts.append(contact)

    return contacts


def contacts_to_pickle(contacts, path):
    # The "wb" indicates that the file will be opened in binary write mode
    with open(path, mode="wb") as file:
        # The ".dump()" function write a file and transforms the data to binary data that is understood by Python
        pickle.dump(contacts, file)


def pickle_to_contacts(path):
    # The "wb" indicates that the file will be opened in binary reading mode
    with open(path, mode="rb") as file:
        # The ".load()" function read a Pickle file and transforms the data of the file to objects in Python
        contacts = pickle.load(file)

        return contacts
