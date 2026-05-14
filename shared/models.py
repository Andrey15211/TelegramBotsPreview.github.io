from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    service_name: Mapped[str] = mapped_column(String(160))
    price: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(32), default="new")
