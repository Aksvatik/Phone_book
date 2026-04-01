def ask_continue(question: str) -> bool:
    while True:
        cmd = input(f"{question}\nВыберите действие (0 - нет, 1 - да): ").strip()
        match cmd:
            case "0":
                print("")
                return False
            case "1":
                return True
            case _:
                print("Ошибка. Такого действия нет, введите повторно.\n")