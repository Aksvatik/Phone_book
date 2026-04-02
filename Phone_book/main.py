import json_tools
import book_logic
import utilities
# import sys
# import os


MENU = ("1 - Показать все контакты\n"
        "2 - Добавить новый контакт\n"
        "3 - Найти контакт\n"
        "4 - Удалить контакт\n"
        "0 - Выход\n")

# Загрузка контактов
contacts = json_tools.load_json()

print(MENU)

while True:
    command = input("Выберите действие: ")
    match command:
        case "1":
            if contacts:
                for contact in contacts:
                    print(book_logic.print_contact(contact))
                print("")
            else:
                print("У вас нет контактов.\n")

        case "2":
            print("ЕЩЕ НЕ ГОТОВО\n")

        case "3":
            while True:
                name = input("Введите имя контакта: ").lower().strip()
                name_list = book_logic.find_contacts(contacts, name)
                if name_list:
                    for contact in name_list:
                        print(book_logic.print_contact(contact))
                        continue
                    print("")
                else:
                    print("Контакт не найден. Попробуйте еще раз.\n")

                if not utilities.ask_continue("Хотите найти еще один контакт?"):
                    break
                else:
                    pass

        case "4":
            while True:
                name = input("Введите имя контакта: ").lower().strip()
                name_list = book_logic.find_contacts(contacts, name)
                # Если контакт не существует
                if not name_list:
                    print("Контакт не найден. Попробуйте еще раз.\n")
                    continue

                # Если контакт удаления определен
                if len(name_list) == 1:
                    if utilities.ask_continue(f"Вы точно хотите удалить контакт: {name.title()}"):
                        book_logic.delete_contact(contacts, name)
                    else:
                        pass

                # Если контакт удаления не определен
                if len(name_list) > 1:
                    print("Точного совпадения не найдено. Возможно вы имели ввиду, кого-то из этих контактов:")
                    for contact in name_list:
                        print(book_logic.print_contact(contact))
                    print("")
                    continue

                # Вопрос перед выходом
                if not utilities.ask_continue("Хотите удалить еще один контакт?"):
                    break
                else:
                    pass

        case "0":
            json_tools.dump_json(contacts)
            break

        case _:
            print("Такого действия нет, попробуйте еще раз")