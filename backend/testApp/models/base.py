from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,declared_attr
from sqlalchemy import String, Integer

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True)