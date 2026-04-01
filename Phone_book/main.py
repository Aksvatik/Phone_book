import json_tools
import book_logic
import utilities
import sys
import os


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

                if not utilities.ask_continue("Хотите изменить фильтр сортировки?"):
                    pass
                else:
                    print("ЕЩЕ НЕ ГОТОВО\n")
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
            print("ЕЩЕ НЕ ГОТОВО\n")

        case "0":
            break

        case _:
            print("Такого действия нет, попробуйте еще раз")