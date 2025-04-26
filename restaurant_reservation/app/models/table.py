from app.database import Base
from sqlalchemy import Column, Integer, String


class Table(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    seats = Column(Integer, nullable=False)
    location = Column(String(100))