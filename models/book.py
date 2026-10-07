"""Книга: модель и операции сравнения, хеширования и вывода."""

from models.printed_edition import PrintedEdition
from models.validation import validate_int, validate_text, PAGES_MIN, PAGES_MAX


class Book(PrintedEdition):
    """Книга. Собственные поля: author, pages."""

    author: str
    pages: int

    def __init__(
        self,
        name: str = "Без названия",
        pub_year: int = 2000,
        author: str = "Неизвестный автор",
        pages: int = 1,
    ):
        super().__init__(name, pub_year)
        self.author = validate_text(author, "автор")
        self.pages = validate_int(pages, "страниц", PAGES_MIN, PAGES_MAX)

    def __eq__(self, other: object):
        """Сравнивает конкретный тип и все поля, включая унаследованные."""
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.name,
            self.pub_year,
            self.author,
            self.pages,
        ) == (
            other.name,
            other.pub_year,
            other.author,
            other.pages,
        )

    def __hash__(self) -> int:
        """Хеширует тип и те же поля, которые участвуют в равенстве."""
        return hash((type(self), self.name, self.pub_year, self.author, self.pages))

    def __str__(self) -> str:
        """Возвращает вид издания и значения всех полей."""
        return (
            f"Книга: название={self.name!r}"
            f", год={self.pub_year}"
            f", автор={self.author!r}"
            f", страниц={self.pages}"
        )
