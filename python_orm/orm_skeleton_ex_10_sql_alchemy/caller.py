from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe, Chef

engine = create_engine('postgresql+psycopg2://user:password@localhost/10-SQL-Alchemy-Ex')
Session = sessionmaker(bind=engine)

session = Session()

# Task 02
@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )

    session.add(new_recipe)


# recipe1 = create_recipe('Spaghetti Carbonara', 'Pasta, Eggs, Pancetta, Cheese', 'Cook the pasta, mix it with eggs, pancetta, and cheese')
# recipe2 = create_recipe('Chicken Stir-Fry', 'Chicken, Bell Peppers, Soy Sauce, Vegetables', 'Stir-fry chicken and vegetables with soy sauce')
# recipe3 = create_recipe('Caesar Salad', 'Romaine Lettuce, Croutons, Caesar Dressing', 'Toss lettuce with dressing and top with croutons')



# Task 03
@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str):
    records_changed: int = (
        session.query(Recipe).filter_by(name=name).update(
            {
                Recipe.name: new_name,
                Recipe.ingredients: new_ingredients,
                Recipe.instructions: new_name,
            }
        )
    )
    
    # recipe_to_update = session.query(Recipe).filter_by(name=name).first() # SELECT
    # recipe_to_update.name = new_name
    # recipe_to_update.ingredients = new_ingredients
    # recipe_to_update.instructions = new_instructions

    return records_changed


# # Update a recipe by name
# update_recipe_by_name(
#     name="Spaghetti Carbonara",
#     new_name="Carbonara Pasta",
#     new_ingredients="Pasta, Eggs, Guanciale, Cheese",
#     new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
# )

# # Query the updated recipe 
# updated_recipe = session.query(Recipe).filter_by(name="Carbonara Pasta").first()

# # Print the updated recipe details
# print("Updated Recipe Details:")
# print(f"Name: {updated_recipe.name}")
# print(f"Ingredients: {updated_recipe.ingredients}")
# print(f"Instructions: {updated_recipe.instructions}")



# Task 04
@session_decorator(session)
def delete_recipe_by_name(name: str):
    changed_records: int = (
        session.query(Recipe).filter_by(
            name=name,
        ).delete()
    )

    return changed_records


# # Delete a recipe by name
# delete_recipe_by_name("Carbonara Pasta")

# # Query all recipes
# recipes = session.query(Recipe).all()

# # Loop through each recipe and print its details
# for recipe in recipes:
#     print(f"Recipe name: {recipe.name}")



# Task 05
with Session() as session:

    # def get_recipes_by_ingredient(ingredient_name: str):
    #     recipes_with_ingredient = (
    #         session.query(Recipe).filter(
    #             Recipe.ingredients.ilike(f'%{ingredient_name}%')
    #         ).all()
    #     )

    #     return recipes_with_ingredient


    # # Delete all objects (recipes) from the database
    # session.query(Recipe).delete()
    # session.commit()

    # # Create three Recipe instances with two of them sharing the same ingredient
    # recipe1 = create_recipe(
    #     'Spaghetti Bolognese',
    #     'Ground beef, tomatoes, pasta',
    #     'Cook beef, add tomatoes, serve over pasta'
    # )

    # recipe2 = create_recipe(
    #     'Chicken Alfredo',
    #     'Chicken, fettuccine, Alfredo sauce',
    #     'Cook chicken, boil pasta, mix with sauce'
    # )

    # recipe3 = create_recipe(
    #     'Chicken Noodle Soup',
    #     'Chicken, noodles, carrots',
    #     'Boil chicken, add noodles, carrots'
    # )

    # # Run the function and print the results
    # ingredient_to_filter = 'Chicken'
    # filtered_recipes = get_recipes_by_ingredient('Chicken')

    # print(f"Recipes containing {ingredient_to_filter}:")
    # for recipe in filtered_recipes:
    #     print(f"Recipe name - {recipe.name}")
    pass


# Task 06
@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    first_r = (
        session.query(Recipe).filter_by(
            name=first_recipe_name,
        ).with_for_update().one()
    )

    second_r = (
        session.query(Recipe).filter_by(
            name=second_recipe_name,
        ).with_for_update().one()
    )

    first_r.ingredients, second_r.ingredients = second_r.ingredients, first_r.ingredients


# # Delete all objects (recipes) from the database
# session.query(Recipe).delete()
# session.commit()

# # Create the first recipe
# create_recipe("Pancakes", "Flour, Eggs, Milk", "Mix and cook on a griddle")

# # Create the second recipe
# create_recipe("Waffles", "Flour, Eggs, Milk, Baking Powder", "Mix and cook in a waffle iron")

# # Now, swap their ingredients
# swap_recipe_ingredients_by_name("Pancakes", "Waffles")

# recipe1 = session.query(Recipe).filter_by(name="Pancakes").first()
# recipe2 = session.query(Recipe).filter_by(name="Waffles").first()
# print(f"Pancakes ingredients {recipe1.ingredients}")
# print(f"Waffles ingredients {recipe2.ingredients}")



# Task 09
@session_decorator(session)
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe and recipe.chef:
        return f'Recipe: {recipe_name} already has a related chef'
    
    chef = session.query(Chef).filter_by(name=chef_name).first()

    recipe.chef = chef
    return f'Related recipe {recipe_name} with chef {chef_name}'


# # Create a recipe instance for Bulgarian Musaka
# musaka_recipe = Recipe(
#     name="Musaka",
#     ingredients="Potatoes, Ground Meat, Onions, Eggs, Milk, Cheese, Spices",
#     instructions="Layer potatoes and meat mixture, pour egg and milk mixture on top, bake until golden brown."
# )

# # Create a Bulgarian chef instances
# bulgarian_chef1 = Chef(name="Ivan Zvezdev")
# bulgarian_chef2 = Chef(name="Uti Buchvarov")

# # Add the recipe instance to the session
# session.add(musaka_recipe)

# # Add the chef instances to the session
# session.add(bulgarian_chef1)
# session.add(bulgarian_chef2)

# # Commit the changes to the database
# session.commit()

# print(relate_recipe_with_chef_by_name("Musaka", "Ivan Zvezdev"))
# print(relate_recipe_with_chef_by_name("Musaka", "Chef Uti"))



# Task 10
@session_decorator(session)
def get_recipes_with_chef():
    recipes_with_chef = (
        session.query(Recipe.name, Chef.name.label('chef_name')).join(
            Chef,
            Recipe.chef
        ).all()
    )

    return '\n'.join(f'Recipe: {recipe_name} made by chef: {chef_name}' for recipe_name, chef_name in recipes_with_chef)


# # Delete all objects (recipes and chefs) from the database
# session.query(Recipe).delete()
# session.query(Chef).delete()
# session.commit()

# # Create chef instances
# chef1 = Chef(name="Gordon Ramsay")
# chef2 = Chef(name="Julia Child")
# chef3 = Chef(name="Jamie Oliver")
# chef4 = Chef(name="Nigella Lawson")

# # Create recipe instances associated with chefs
# recipe1 = Recipe(name="Beef Wellington", ingredients="Beef fillet, Puff pastry, Mushrooms, Foie gras", instructions="Prepare the fillet and encase it in puff pastry.")
# recipe1.chef = chef1

# recipe2 = Recipe(name="Boeuf Bourguignon", ingredients="Beef, Red wine, Onions, Carrots", instructions="Slow-cook the beef with red wine and vegetables.")
# recipe2.chef = chef2

# recipe3 = Recipe(name="Spaghetti Carbonara", ingredients="Spaghetti, Eggs, Pancetta, Cheese", instructions="Cook pasta, mix ingredients.")
# recipe3.chef = chef3

# recipe4 = Recipe(name="Chocolate Cake", ingredients="Chocolate, Flour, Sugar, Eggs", instructions="Bake a delicious chocolate cake.")
# recipe4.chef = chef4

# recipe5 = Recipe(name="Chicken Tikka Masala", ingredients="Chicken, Yogurt, Tomatoes, Spices", instructions="Marinate chicken and cook in a creamy tomato sauce.")
# recipe5.chef = chef3

# session.add_all([chef1, chef2, chef3, chef4, recipe1, recipe2, recipe3, recipe4, recipe5])
# session.commit()
# print(get_recipes_with_chef())
