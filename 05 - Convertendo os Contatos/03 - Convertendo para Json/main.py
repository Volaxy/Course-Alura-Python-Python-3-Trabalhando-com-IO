import contacts_util


def __main__():
    # contacts = contacts_util.csv_to_contact("data/contacts.csv")

    # contacts_util.contacts_to_pickle(contacts, "data/contacts.pickle")
    # contacts = contacts_util.pickle_to_contacts("data/contacts.pickle")

    # contacts_util.contacts_to_json(contacts, "data/contacts.json")

    contacts = contacts_util.json_to_contacts("data/contacts.json")

    for contact in contacts:
        print(f"Id: {contact.id}, Name: {contact.name}, E-mail: {contact.email}")


if __name__ == "__main__":
    __main__()
