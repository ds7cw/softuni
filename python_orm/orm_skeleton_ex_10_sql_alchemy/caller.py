from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe

engine = create_engine('postgresql+psycopg2://user:pass@localhost/10-SQL-Alchemy-Ex')
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )

    session.add(new_recipe)


recipe1 = create_recipe('Spaghetti Carbonara', 'Pasta, Eggs, Pancetta, Cheese', 'Cook the pasta, mix it with eggs, pancetta, and cheese')
recipe2 = create_recipe('Chicken Stir-Fry', 'Chicken, Bell Peppers, Soy Sauce, Vegetables', 'Stir-fry chicken and vegetables with soy sauce')
recipe3 = create_recipe('Caesar Salad', 'Romaine Lettuce, Croutons, Caesar Dressing', 'Toss lettuce with dressing and top with croutons')
