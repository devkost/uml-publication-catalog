"""Журнал: модель и операции сравнения, хеширования и вывода."""

from models.printed_edition import PrintedEdition
from models.validation import validate_int, validate_text, ISSUE_MIN, ISSUE_MAX


class Magazine(PrintedEdition):
    """Журнал. Собственные поля: release_num, periodicity."""

    release_num: int
    periodicity: str

    def __init__(
        self,
        name: str = "Без названия",
        pub_year: int = 2000,
        release_num: int = 1,
        periodicity: str = "Ежемесячно",
    ):
        super().__init__(name, pub_year)
        self.release_num = validate_int(release_num, "выпуск", ISSUE_MIN, ISSUE_MAX)
        self.periodicity = validate_text(periodicity, "периодичность")

    def __eq__(self, other: object):
        """Сравнивает конкретный тип и все поля, включая унаследованные."""
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.name,
            self.pub_year,
            self.release_num,
            self.periodicity,
        ) == (
            other.name,
            other.pub_year,
            other.release_num,
            other.periodicity,
        )

    def __hash__(self) -> int:
        """Хеширует тип и те же поля, которые участвуют в равенстве."""
        return hash((type(self), self.name, self.pub_year, self.release_num, self.periodicity))

    def __str__(self) -> str:
        """Возвращает вид издания и значения всех полей."""
        return (
            f"Журнал: название={self.name!r}"
            f", год={self.pub_year}"
            f", выпуск={self.release_num}"
            f", периодичность={self.periodicity!r}"
        )
