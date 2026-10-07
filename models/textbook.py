"""Учебник: модель и операции сравнения, хеширования и вывода."""

from models.book import Book
from models.validation import validate_int, validate_text, GRADE_MIN, GRADE_MAX


class Textbook(Book):
    """Учебник. Собственные поля: subject, grade."""

    subject: str
    grade: int

    def __init__(
        self,
        name: str = "Без названия",
        pub_year: int = 2000,
        author: str = "Неизвестный автор",
        pages: int = 1,
        subject: str = "Общий предмет",
        grade: int = 1,
    ):
        super().__init__(name, pub_year, author, pages)
        self.subject = validate_text(subject, "предмет")
        self.grade = validate_int(grade, "класс", GRADE_MIN, GRADE_MAX)

    def __eq__(self, other: object):
        """Сравнивает конкретный тип и все поля, включая унаследованные."""
        if type(self) is not type(other):
            return NotImplemented
        return (
            self.name,
            self.pub_year,
            self.author,
            self.pages,
            self.subject,
            self.grade,
        ) == (
            other.name,
            other.pub_year,
            other.author,
            other.pages,
            other.subject,
            other.grade,
        )

    def __hash__(self) -> int:
        """Хеширует тип и те же поля, которые участвуют в равенстве."""
        return hash((type(self), self.name, self.pub_year, self.author, self.pages, self.subject, self.grade))

    def __str__(self) -> str:
        """Возвращает вид издания и значения всех полей."""
        return (
            f"Учебник: название={self.name!r}"
            f", год={self.pub_year}"
            f", автор={self.author!r}"
            f", страниц={self.pages}"
            f", предмет={self.subject!r}"
            f", класс={self.grade}"
        )
