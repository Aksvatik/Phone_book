import json_tools
import book_logic
import utilities


# Отчистка приглашения командной строки при запуске
utilities.clear_cmd()

MENU = ("===================== МЕНЮ =====================\n\n"
        "1 - Показать все контакты\n"
        "2 - Добавить новый контакт\n"
        "3 - Найти контакт\n"
        "4 - Удалить контакт\n"
        "0 - Выход\n")

# Загрузка контактов
contacts = json_tools.load_json()

while True:
    print(MENU)
    command = input("Выберите действие: ")
    match command:
        case "1":
            utilities.clear_cmd()
            print("================= ВСЕ КОНТАКТЫ =================\n")

            if contacts:
                for contact in range(len(contacts)):
                    print(f"{contact + 1}. {book_logic.print_contact(contacts[contact])}")
                print("")
            else:
                print("У вас нет контактов.\n")

            if not utilities.ask_continue("Нажмите Enter, чтобы продолжить...", False):
                utilities.clear_cmd()
                continue

        # Еще не готово
        case "2":
            utilities.clear_cmd()
            print("===========ДОБАВЛЕНИЕ НОВОГО КОНТАКТА===========\n")
            print("ЕЩЕ НЕ ГОТОВО\n")

            if not utilities.ask_continue("Нажмите Enter, чтобы продолжить...", False):
                utilities.clear_cmd()
                continue

        case "3":
            while True:
                utilities.clear_cmd()
                print("============== ПОИСК ПО КОНТАКТАМ ==============\n")

                name = input("Введите имя контакта (для выхода введите - q): ").lower().strip()

                # Выход без поиска контакта
                if name in ["q", "quit", "й", "йгше", "0"]:
                    utilities.clear_cmd()
                    break

                print("")
                name_list = book_logic.find_contacts(contacts, name.split())

                # Поиск контакта
                if name_list:
                    for contact in range(len(name_list)):
                        print(f"{contact + 1}. {book_logic.print_contact(name_list[contact])}")
                        continue
                    print("")
                else:
                    print("Контакт не найден. Попробуйте еще раз.\n")

                # Вопрос перед выходом
                if not utilities.ask_continue("Хотите найти еще один контакт?"):
                    utilities.clear_cmd()
                    break
                else:
                    utilities.clear_cmd()
                    pass

        case "4":
            utilities.clear_cmd()
            print("============== УДАЛЕНИЕ КОНТАКТА ===============\n")
            while True:

                name = input("Введите имя контакта (для выхода введите - q): ").lower().strip()

                # Выход без удаления контакта
                if name in ["q", "quit", "й", "йгше", "0"]:
                    utilities.clear_cmd()
                    break

                print("")
                name_list = book_logic.find_contacts(contacts, name.split())


                if name_list:
                    # Если найдено точное совпадение
                    if len(name_list) == 1:
                        if utilities.ask_continue(f"Вы точно хотите удалить контакт: {name_list[0]["name"].title()}"):
                            print("")
                            book_logic.delete_contact(contacts, name_list[0]["name"])
                        pass

                    # Если найдено частичное совпадение
                    if len(name_list) > 1:
                        for contact in range(len(name_list)):
                            print(f"{contact + 1}. {book_logic.print_contact(name_list[contact])}")
                        print("")
                        continue
                else:
                    print("Контакт не найден. Попробуйте еще раз.\n")
                    continue

                # Вопрос перед выходом
                if not utilities.ask_continue("Хотите удалить еще один контакт?"):
                    utilities.clear_cmd()
                    break
                else:
                    print("")
                    pass

        case "0" | "q" | "й":
            # Сохранение контактов
            json_tools.dump_json(contacts)
            break

        case _:
            print("Такого действия нет, попробуйте еще раз")