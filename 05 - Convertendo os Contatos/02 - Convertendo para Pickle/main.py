import contacts_util


def __main__():
    # contacts = contacts_util.csv_to_contact("data/contacts.csv")

    # The extension of Pickle files is the "*.p" or "*.pickle"
    # contacts_util.contacts_to_pickle(contacts, "data/contacts.pickle")

    # It's very important knows the source of the file, because the file can be contained malicious code like invasions
    contacts = contacts_util.pickle_to_contacts("data/contacts.pickle")

    for contact in contacts:
        print(f"Id: {contact.id}, Name: {contact.name}, E-mail: {contact.email}")


if __name__ == "__main__":
    __main__()
