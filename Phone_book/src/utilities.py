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


def delete_space(string: str) -> str:
    string = list(string)

    index_space = [i for i in range(len(string) - 1) if string[i] == " "]

    if not index_space:
        return "".join(string)

    index_space.remove(min(index_space))

    while index_space:
        string.pop(index_space[0])
        index_space.pop()

    return "".join(string)


def is_quit(var: str) -> bool:
    if var in ["q", "quit", "й", "йгше", "0", "Q", "Й"]:
        return True
    return False