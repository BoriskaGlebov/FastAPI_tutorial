from sqlalchemy import text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base, str_uniq, int_pk, str_null_true
from app.students.models import Student


# создаем модель таблицы факультетов (majors)
class Major(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    major_name: Mapped[str_uniq]
    major_description: Mapped[str_null_true]
    count_students: Mapped[int] = mapped_column(server_default=text('0'))
    students:Mapped[list[Student]]=relationship('Student',back_populates='major')
    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)

if __name__ == '__main__':
    Base.metadata.create_all(engine)