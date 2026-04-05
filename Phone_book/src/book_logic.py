# import json_tools


def print_contact(contact) -> str:
    return (
        f"{contact['name'].title()}: "
        f"+7 ({contact['phone_number'][0:3]}) {contact['phone_number'][3:6]}-"
        f"{contact['phone_number'][6:8]}-{contact['phone_number'][8:10]}"
    )


def find_contacts(contacts, name: list) -> list:
    if not name:
        return []

    found_contacts = []

    for contact in contacts:
        if all(word in contact["name"] for word in name):
            found_contacts.append(contact)

    return found_contacts


def add_contact():
    pass


def delete_contact(contacts, name) -> None:
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)


# test = json_tools.load_json()
# print(test)
#
# delete_contact(test, "александр шмелев")
# print(test)