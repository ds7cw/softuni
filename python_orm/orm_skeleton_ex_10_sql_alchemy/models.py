from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class Recipe(Base): # Task 01
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

    # Task 08
    chef_id = Column(
        Integer,
        ForeignKey('chefs.id')
    )

    chef = relationship('Chef', back_populates='recipes')


class Chef(Base): # Task 07
    __tablename__ = 'chefs'

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False,
    )

    recipes = relationship('Recipe', back_populates='chef')