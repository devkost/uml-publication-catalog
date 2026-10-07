"""Печатное издание: модель и операции сравнения, хеширования и вывода."""

from models.validation import validate_int, validate_text, YEAR_MIN, YEAR_MAX


class PrintedEdition:
    """Печатное издание. Собственные поля: name, pub_year."""

    name: str
    pub_year: int

    def __init__(
        self,
        name: str = "Без названия",
        pub_year: int = 2000,
    ):
        self.name = validate_text(name, "название")
        self.pub_year = validate_int(pub_year, "год", YEAR_MIN, YEAR_MAX)

    def __eq__(self, other: object):
        """Сравнивает конкретный тип и все поля, включая унаследованные."""
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.name,
            self.pub_year,
        ) == (
            other.name,
            other.pub_year,
        )

    def __hash__(self) -> int:
        """Хеширует тип и те же поля, которые участвуют в равенстве."""
        return hash((type(self), self.name, self.pub_year))

    def __str__(self) -> str:
        """Возвращает вид издания и значения всех полей."""
        return (
            f"Печатное издание: название={self.name!r}"
            f", год={self.pub_year}"
        )
