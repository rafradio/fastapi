# import sqlalchemy
# from typing import List
# from typing import Optional
# from sqlalchemy.orm import Mapped
# from sqlalchemy.orm import mapped_column
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import DeclarativeBase

# from sqlalchemy import ForeignKey
# from sqlalchemy import Integer

from __future__ import annotations
from typing import List
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import Integer, String, Text, Float, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship



class Base(DeclarativeBase):
    pass

# Base = declarative_base()
# db = sqlalchemy()

class Client(Base):
    __tablename__ = "clients"
    # __table_args__ = {'schema': 'public'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(80))
    second_name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(120))
    password: Mapped[str] = mapped_column(String(20))
    orders: Mapped[List["Order"]] = relationship(back_populates="client")

class Merchant(Base):
    __tablename__ = "merchants"
    # __table_args__ = {'schema': 'public'}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text())
    price: Mapped[float] = mapped_column(Float(precision=2))
    orders: Mapped[List["Order"]] = relationship(back_populates="merchant")
    
class Order(Base):
    __tablename__ = 'orders'
    # __table_args__ = {'schema': 'public'}
    id: Mapped[int] = mapped_column(primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    merchant_id: Mapped[int] = mapped_column(ForeignKey("merchants.id"))
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    status: Mapped[str] = mapped_column(String(40))
