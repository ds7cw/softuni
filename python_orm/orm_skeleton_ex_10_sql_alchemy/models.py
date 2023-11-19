from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(
        Integer,
        primary_key=True,
    )

    name = Column(
        String(100),
        nullable=False
    )

    ingredients = Column(
        Text,
        nullable=False
    )

    instructions = Column(
        Text,
        nullable=False
    )