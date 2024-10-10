from sqlalchemy import ForeignKey, text, Text, Integer
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true, engine
from datetime import date


# создаем модель таблицы студентов
class Student(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]= mapped_column(nullable=False)
    last_name: Mapped[str]= mapped_column(nullable=False)
    date_of_birth: Mapped[date]= mapped_column(nullable=False)
    email: Mapped[str_uniq]
    address: Mapped[str] = mapped_column(Text, nullable=False)
    enrollment_year: Mapped[int]= mapped_column(nullable=False)
    course: Mapped[int]= mapped_column(nullable=False)
    special_notes: Mapped[str_null_true] = str_null_true
    major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)

    major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    Base.metadata.create_all(engine)