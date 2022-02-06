import contacts_util


def __main__():
    contacts = contacts_util.csv_to_contact("data/contacts.csv")

    for contact in contacts:
        print(f"Id: {contact.id}, Name: {contact.name}, E-mail: {contact.email}")


if __name__ == "__main__":
    __main__()
