from typing import Optional

from sqlalchemy import Index, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER, LONGBLOB
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('country_code', 'country_code', 'phone_number', unique=True),
        Index('email', 'email', unique=True)
    )

    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[str] = mapped_column(String(100))
    nickname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    country_code: Mapped[str] = mapped_column(String(6))
    phone_number: Mapped[str] = mapped_column(String(20))
    country: Mapped[str] = mapped_column(String(100))
    profile_photo: Mapped[Optional[bytes]] = mapped_column(LONGBLOB)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
