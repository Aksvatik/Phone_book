# Телефонный справочник

Консольное приложение для управления контактами: добавление, редактирование, поиск и удаление записей.

## Возможности
- Просмотр всех контактов
- Создание новой записи
- Поиск контакта по имени или телефону
- Удаление контакта из базы

## Установка

1. Клонируйте репозиторий:

      ```bash
      git clone https://github.com/Aksvatik/Phone_book.git
      cd Phone_book/Phone_book
      ```

2. Создайте виртуальное окружение:
   1. Для Windows:
   
      ```cmd
      python -m venv .venv
      .venv\Scripts\activate
      ```
   2. Для Linux/MacOS
   
      ```bash
      python -m venv .venv
      source .venv/bin/activate
      ```
3. Зависимостей сторонних библиотек нет

## Использование
1. Смените директорию

      ```bash
      cd src
      ```

2. Запустите приложение:

      ```bash
      python main.py
      ```

3. Следуйте инструкциям

## Структура проекта
```
Phone_book/
├── Phone_book/
│   ├── src/
│   │   ├── book_logic.py    # Логика
│   │   ├── json_tools.py    # Работа с json
│   │   ├── main.py          # Меню
│   │   └── utilities.py     # Валидация, форматирование
│   └── data/
│       └── contacts.json    # Хранилище контактов
├── .gitignore
└── README.md
```