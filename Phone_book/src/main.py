import json_tools
import book_logic
import utilities


MENU = ("===================== МЕНЮ =====================\n\n"
        "1 - Показать все контакты\n"
        "2 - Добавить новый контакт\n"
        "3 - Найти контакт\n"
        "4 - Удалить контакт\n"
        "0 - Выход\n")

# Загрузка контактов
contacts = json_tools.load_json()

while True:
    utilities.clear_cmd()
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

        case "2":
            while True:
                utilities.clear_cmd()
                print("=========== ДОБАВЛЕНИЕ НОВОГО КОНТАКТА ===========\n")

                # Ввод имени
                name = None
                while True:
                    tmp_name = input("Введите имя контакта (для выхода введите q): ").lower().strip()
                    print("")

                    # Выход без создания контакта
                    if utilities.is_quit(tmp_name):
                        name = None
                        break

                    name = utilities.delete_space(tmp_name)

                    if not name:
                        continue
                    break

                # Выход в меню
                if name is None:
                    break

                # Проверка на точное совпадение имени
                name_list = book_logic.find_contacts(contacts, name.split())

                if len(name_list) == 1:
                    print(
                        f"Такое имя контакта уже существует:\n"
                        f"{book_logic.print_contact(name_list[0])}\n"
                    )
                    if not utilities.ask_continue("Вы уверены, что хотите продолжить создание контакта?"):
                        break

                # Ввод телефона
                phone = None
                while True:
                    tmp_phone = input("Введите номер телефона (для выхода введите q): +7").strip()
                    print("")

                    # Выход без создания контакта
                    if utilities.is_quit(tmp_phone):
                        phone = None
                        break

                    if not tmp_phone or not tmp_phone.isnumeric() or len(tmp_phone) != 10:
                        print("Некорректный номер телефона. Попробуйте еще раз.\n")
                        continue

                    if any(c["phone_number"] == tmp_phone for c in contacts):
                        print("Контакт с таким номером уже существует.\n")
                        input("Нажмите Enter, чтобы продолжить...")
                        print("")
                        phone = None
                        break

                    phone = tmp_phone
                    break

                if phone is None:
                    break

                book_logic.add_contact(contacts, name, phone)
                print(f"\nКонтакт {name.title()} успешно добавлен.\n")

                # Вопрос о продолжении
                if not utilities.ask_continue("Хотите добавить еще один контакт?"):
                    utilities.clear_cmd()
                    break

        case "3":
            while True:
                utilities.clear_cmd()
                print("============== ПОИСК ПО КОНТАКТАМ ==============\n")

                name = input("Введите имя контакта (для выхода введите - q): ").lower().strip()

                # Выход без поиска контакта
                if utilities.is_quit(name):
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

                # Вопрос о продолжении
                if not utilities.ask_continue("Хотите добавить еще один контакт?"):
                    utilities.clear_cmd()
                    break

        case "4":
            utilities.clear_cmd()
            print("============== УДАЛЕНИЕ КОНТАКТА ===============\n")
            while True:

                name = input("Введите имя контакта (для выхода введите - q): ").lower().strip()

                # Выход без удаления контакта
                if utilities.is_quit(name):
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

                # Вопрос о продолжении
                if not utilities.ask_continue("Хотите удалить еще один контакт?"):
                    utilities.clear_cmd()
                    break

        case "0" | "q" | "й":
            # Сохранение контактов
            json_tools.dump_json(contacts)
            break

        case _:
            pass