import csv
import pickle
import json

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
    with open(path, mode="wb") as file:
        pickle.dump(contacts, file)


def pickle_to_contacts(path):
    with open(path, mode="rb") as file:
        contacts = pickle.load(file)

        return contacts


def contacts_to_json(contacts, path):
    with open(path, mode="w") as file:
        # The "json.dump()" transforms the data to json file
        json.dump(contacts, file, default=_contact_to_json)


def _contact_to_json(contact):
    # The "__dict__" return the objects represented by a dictionary
    return contact.__dict__


def json_to_contacts(path):
    contacts = []

    with open(path) as file:
        # The function "json.load()" read a file and
        contacts_json = json.load(file)

        for contact in contacts_json:
            # If the name of the attributes is the same as the name of the keys in the dictionary, you can use wrapping,
            # putting "**" in front of the variable when creating the object
            # c = Contact(**contact)

            c = Contact(contact["id"], contact["name"], contact["email"])

            contacts.append(c)

    return contacts
