import os


def ask_continue(question: str, is_choice=True) -> bool:
    while True:
        if is_choice:
            cmd = input(f"{question}\nВыберите действие (0 - нет, 1 - да): ").strip()
            match cmd:
                case "0":
                    print("")
                    return False
                case "1":
                    return True
                case _:
                    print("Ошибка. Такого действия нет, введите повторно.\n")
        else:
            input(question).strip()
            return False


def clear_cmd() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')