"""Ввод данных и меню. Коллекция существует до завершения программы."""

from models import PrintedEdition, Magazine, Book, Textbook
from models.validation import (
    YEAR_MIN, YEAR_MAX, ISSUE_MIN, ISSUE_MAX,
    PAGES_MIN, PAGES_MAX, GRADE_MIN, GRADE_MAX,
)


def read_int(prompt: str, minimum: int, maximum: int) -> int:
    """Повторяет ввод до получения целого числа в включительном диапазоне."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"Ошибка: допустимы значения от {minimum} до {maximum}.")


def read_text(prompt: str) -> str:
    """Считывает непустую строку, удаляя крайние пробелы."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Ошибка: строка не должна быть пустой.")


def add_edition(editions: list[PrintedEdition]) -> None:
    """Создаёт объект выбранного вида и добавляет его в общий список."""
    print("\n1. Печатное издание\n2. Журнал\n3. Книга\n4. Учебник\n0. Назад")
    kind = read_int("Выберите тип издания: ", 0, 4)
    if kind == 0:
        return
    name = read_text("Название: ")
    year = read_int("Год публикации: ", YEAR_MIN, YEAR_MAX)
    if kind == 1:
        edition = PrintedEdition(name, year)
    elif kind == 2:
        periodicity = read_text("Периодичность: ")
        issue = read_int("Номер выпуска: ", ISSUE_MIN, ISSUE_MAX)
        edition = Magazine(name, year, issue, periodicity)
    else:
        author = read_text("Автор: ")
        pages = read_int("Количество страниц: ", PAGES_MIN, PAGES_MAX)
        if kind == 3:
            edition = Book(name, year, author, pages)
        else:
            subject = read_text("Предмет: ")
            grade = read_int("Номер класса: ", GRADE_MIN, GRADE_MAX)
            edition = Textbook(name, year, author, pages, subject, grade)
    editions.append(edition)
    print("Элемент добавлен.")


def show_editions(editions: list[PrintedEdition]) -> None:
    """Выводит объекты с индексами, вызывая их собственные __str__."""
    if not editions:
        print("Коллекция пуста.")
        return
    for index, edition in enumerate(editions):
        print(f"[{index}] {edition}")


def delete_edition(editions: list[PrintedEdition]) -> None:
    """Удаляет объект по проверенному неотрицательному индексу."""
    show_editions(editions)
    if not editions:
        return
    index = read_int("Индекс удаляемого элемента: ", 0, len(editions) - 1)
    editions.pop(index)
    print("Элемент удалён.")


def compare_editions(editions: list[PrintedEdition]) -> None:
    """Сравнивает значения двух объектов; одинаковые индексы разрешены."""
    show_editions(editions)
    if not editions:
        return
    first = read_int("Индекс первого элемента: ", 0, len(editions) - 1)
    second = read_int("Индекс второго элемента: ", 0, len(editions) - 1)
    print("Элементы равны." if editions[first] == editions[second]
          else "Элементы не равны.")


def run_menu() -> None:
    """Запускает меню; EOF и Ctrl+C корректно завершают сеанс."""
    editions: list[PrintedEdition] = []
    actions = {1: add_edition, 2: delete_edition, 3: show_editions, 4: compare_editions}
    try:
        while True:
            print("\n1. Добавить новый элемент\n2. Удалить элемент по индексу"
                  "\n3. Вывести все элементы\n4. Сравнить два элемента по индексам"
                  "\n0. Завершить работу")
            choice = read_int("Выберите действие: ", 0, 4)
            if choice == 0:
                break
            actions[choice](editions)
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван.")
    print("Работа программы завершена.")
