from sqlalchemy import Table, ForeignKey, Column, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    # @declared_attr.directive
    # def __tablename__(cls) -> str:
    #     return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True)


users_matches = Table(
    "users_matches",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("match_id", ForeignKey("match.id"), primary_key=True),
)
