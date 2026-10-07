"""Общие границы и проверки данных модели (границы включительные)."""

YEAR_MIN, YEAR_MAX = 1, 9999
ISSUE_MIN, ISSUE_MAX = 1, 10000
PAGES_MIN, PAGES_MAX = 1, 100000
GRADE_MIN, GRADE_MAX = 1, 11


def validate_int(value: int, label: str, minimum: int, maximum: int) -> int:
    """Возвращает целое число; неверный тип и диапазон вызывают исключения."""
    if type(value) is not int:
        raise TypeError(f"{label}: требуется целое число.")
    if not minimum <= value <= maximum:
        raise ValueError(f"{label}: допустимы значения от {minimum} до {maximum}.")
    return value


def validate_text(value: str, label: str) -> str:
    """Удаляет крайние пробелы и отклоняет неверный тип или пустую строку."""
    if not isinstance(value, str):
        raise TypeError(f"{label}: требуется строка.")
    value = value.strip()
    if not value:
        raise ValueError(f"{label}: строка не должна быть пустой.")
    return value
