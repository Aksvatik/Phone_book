import json


# Конвертация из json в dict
def load_json(path="../data/contacts.json") -> list:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


# Конвертация из dict в json
def dump_json(data: list, path="../data/contacts.json") -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)