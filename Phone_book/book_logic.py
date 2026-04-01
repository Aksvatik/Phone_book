# import json_tools


def print_contact(contact) -> str:
    return (
        f"{contact['name'].title()}: "
        f"+7 ({contact['phone_number'][0:3]}) {contact['phone_number'][3:6]}-"
        f"{contact['phone_number'][6:8]}-{contact['phone_number'][8:10]}"
    )


def find_contacts(contacts, name) -> list:
    # Поиск точного совпадения
    exact_matches = []
    for contact in contacts:
        if contact["name"] == name:
            exact_matches.append(contact)

    # Если точное совпадение найдено, вернет его
    if exact_matches:
        return exact_matches

    # Поиск частичных совпадений
    partial_matches = []
    for contact in contacts:
        if name in contact["name"]:
            partial_matches.append(contact)
    # Возвращает список частичных совпадений, если их нет, то пустой список
    return partial_matches


def add_contact():
    pass


def delete_contact():
    pass


# test = json_tools.load_json()
# print(find_contacts(test, "александр"))