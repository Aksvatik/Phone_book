import json_tools
import book_logic
import utilities


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
            print("ЕЩЕ НЕ ГОТОВО\n")

        case "4":
            print("ЕЩЕ НЕ ГОТОВО\n")

        case "0":
            break

        case _:
            print("Такого действия нет, попробуйте еще раз")