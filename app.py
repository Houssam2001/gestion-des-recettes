# from flask import Flask, request, jsonify
# import json
# from getpass import getpass
#
# app = Flask(__name__)
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.recipe_manager = RecipeManager(username)
#
# def load_users(filename='users.json'):
#     try:
#         with open(filename, 'r') as file:
#             users_data = json.load(file)
#         return {username: User(username, data['password']) for username, data in users_data.items()}
#     except FileNotFoundError:
#         return {}
#
# def save_users(users, filename='users.json'):
#     users_data = {user.username: {'password': user.password} for user in users.values()}
#     with open(filename, 'w') as file:
#         json.dump(users_data, file, indent=2)
#
# class RecipeManager:
#     def __init__(self, filename='recipes.json'):
#         self.filename = filename
#         self.recipes = self.load_recipes()
#
#     def load_recipes(self):
#         try:
#             with open(self.filename, 'r') as file:
#                 recipes = json.load(file)
#             return recipes
#         except FileNotFoundError:
#             return []
#
#     def save_recipes(self):
#         with open(self.filename, 'w') as file:
#             json.dump(self.recipes, file, indent=2)
#
#     def add_recipe(self, name, ingredients, instructions):
#         recipe = {
#             'name': name,
#             'ingredients': ingredients,
#             'instructions': instructions
#         }
#         self.recipes.append(recipe)
#         self.save_recipes()
#         print(f"Recipe '{name}' added successfully!")
#
#     def view_recipes(self):
#         if not self.recipes:
#             print("No recipes available.")
#         else:
#             for i, recipe in enumerate(self.recipes, start=1):
#                 print(f"{i}. {recipe['name']}")
#
#     def search_recipes(self, ingredient):
#         matching_recipes = []
#         for recipe in self.recipes:
#             if any(ingredient.lower() in i.lower() for i in recipe['ingredients']):
#                 matching_recipes.append(recipe)
#
#         if not matching_recipes:
#             print(f"No recipes found with '{ingredient}'.")
#         else:
#             print(f"Recipes containing '{ingredient}':")
#             for recipe in matching_recipes:
#                 print(f"- {recipe['name']}")
#
#     def delete_recipe(self, index):
#         if 1 <= index <= len(self.recipes):
#             deleted_recipe = self.recipes.pop(index - 1)
#             self.save_recipes()
#             print(f"Recipe '{deleted_recipe['name']}' deleted successfully!")
#         else:
#             print("Invalid index. Please enter a valid recipe index.")
#
#     def update_recipe(self, index, name, ingredients, instructions):
#         if 1 <= index <= len(self.recipes):
#             self.recipes[index - 1] = {
#                 'name': name,
#                 'ingredients': ingredients,
#                 'instructions': instructions
#             }
#             self.save_recipes()
#             print(f"Recipe updated successfully!")
#         else:
#             print("Invalid index. Please enter a valid recipe index.")
#
# def get_non_empty_input(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.strip():
#             return user_input
#         else:
#             print("Input cannot be empty. Please try again.")
#
# def get_positive_integer(prompt):
#     while True:
#         user_input = input(prompt)
#         if user_input.isdigit() and int(user_input) > 0:
#             return int(user_input)
#         else:
#             print("Please enter a valid positive integer.")
#
# def login(users):
#     while True:
#         username = input("Enter your username: ")
#         password = getpass("Enter your password: ")
#
#         if username in users and users[username].password == password:
#             print(f"Welcome, {username}!")
#             return users[username]
#         else:
#             print("Invalid username or password. Please try again.")
#
# def register(users):
#     while True:
#         username = input("Enter a new username: ")
#         if username in users:
#             print("Username already exists. Please choose another.")
#             continue
#
#         password = getpass("Enter a password: ")
#         users[username] = User(username, password)
#         save_users(users)
#         print(f"Account for {username} created successfully!")
#         return users[username]
#
# def main():
#     users = load_users()
#     current_user = None
#
#     while True:
#         if current_user is None:
#             print("Login ou Register")
#             print("1. Login")
#             print("2. Register")
#             print("3. Quitter")
#
#             choice = input("Enter votre choix (1-3): ")
#
#             if choice == '1':
#                 current_user = login(users)
#             elif choice == '2':
#                 current_user = register(users)
#             elif choice == '3':
#                 print("Exiting Recipe Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalide choix. Please enter un nombre entre 1 et 3.")
#         else:
#             print("\nRecipe Manager Menu:")
#             print("1. Ajouter une recette")
#             print("2. Voir les recettes")
#             print("3. chercher une recette")
#             print("4. Supprimer une recette")
#             print("5. mettre-a-jour une recette")
#             print("6. Logout")
#             print("7. Quitter")
#
#             choice = input("Enter your choice (1-7): ")
#
#             if choice == '1':
#                 name = get_non_empty_input("Enter recipe name: ")
#                 ingredients = get_non_empty_input("Enter ingredients (comma-separated): ").split(',')
#                 instructions = get_non_empty_input("Enter instructions: ")
#                 current_user.recipe_manager.add_recipe(name, ingredients, instructions)
#             elif choice == '2':
#                 current_user.recipe_manager.view_recipes()
#             elif choice == '3':
#                 ingredient = get_non_empty_input("Enter ingredient to search for: ")
#                 current_user.recipe_manager.search_recipes(ingredient)
#             elif choice == '4':
#                 index = get_positive_integer("Enter the index of the recipe to delete: ")
#                 current_user.recipe_manager.delete_recipe(index)
#             elif choice == '5':
#                 index = get_positive_integer("Enter the index of the recipe to update: ")
#                 name = get_non_empty_input("Enter updated recipe name: ")
#                 ingredients = get_non_empty_input("Enter updated ingredients (comma-separated): ").split(',')
#                 instructions = get_non_empty_input("Enter updated instructions: ")
#                 current_user.recipe_manager.update_recipe(index, name, ingredients, instructions)
#             elif choice == '6':
#                 print(f"Goodbye, {current_user.username}!")
#                 current_user = None
#             elif choice == '7':
#                 print("Exiting Recipe Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalide choix. Please enter un nombre entre 1 and 7.")
#
#
# if __name__ == "__main__":
#     main()

from flask import Flask, request, jsonify
import json
from flask import Flask
from flask_cors import CORS,cross_origin
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
CORS(app)
jwt = JWTManager(app)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.recipe_manager = RecipeManager(username)
def load_users(filename='users.json'):
    try:
        with open(filename, 'r') as file:
            users_data = json.load(file)
        return {username: User(username, data['password']) for username, data in users_data.items()}
    except FileNotFoundError:
        return {}

def save_users(users, filename='users.json'):
    users_data = {user.username: {'password': user.password} for user in users.values()}
    with open(filename, 'w') as file:
        json.dump(users_data, file, indent=2)
def generate_token(username):
    # In a real-world scenario, you'd use a proper authentication library or OAuth2
    return f'{username}_mock_token'

class RecipeManager:
    def __init__(self, username, filename='recipes.json'):
        self.filename = f"{username}_{filename}"
        self.recipes = self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.filename, 'r') as file:
                recipes = json.load(file)
            return recipes
        except FileNotFoundError:
            return []

    def save_recipes(self):
        with open(self.filename, 'w') as file:
            json.dump(self.recipes, file, indent=2)

    def add_recipe(self, name, ingredients, instructions):
        recipe = {
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions
        }
        self.recipes.append(recipe)
        self.save_recipes()
        return f"Recipe '{name}' added successfully!"

    def view_recipes(self):
        if not self.recipes:
            return []
        else:
            return [
                {
                    'name': recipe['name'],
                    'ingredients': (recipe['ingredients']),
                    'instructions': recipe['instructions']
                }
                for recipe in self.recipes
            ]

    def search_recipes(self, ingredient):
        matching_recipes = []
        for recipe in self.recipes:
            if any(ingredient.lower() in i.lower() for i in recipe['ingredients']):
                matching_recipes.append(recipe)

        if not matching_recipes:
            return f"No recipes found with '{ingredient}'."
        else:
            recipe_list = [f"- {recipe['name']}" for recipe in matching_recipes]
            return f"Recipes containing '{ingredient}':\n" + "\n".join(recipe_list)

    def delete_recipe(self, index):
        if 1 <= index <= len(self.recipes):
            deleted_recipe = self.recipes.pop(index - 1)
            self.save_recipes()
            return f"Recipe '{deleted_recipe['name']}' deleted successfully!"
        else:
            return "Invalid index. Please enter a valid recipe index."

    def update_recipe(self, index, name, ingredients, instructions):
        if 1 <= index <= len(self.recipes):
            self.recipes[index - 1] = {
                'name': name,
                'ingredients': ingredients,
                'instructions': instructions
            }
            self.save_recipes()
            return "Recipe updated successfully!"
        else:
            return "Invalid index. Please enter a valid recipe index."

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Please enter a valid positive integer.")

def login(users, username, password):
    if username in users and users[username].password == password:
        return users[username]
    else:
        return None

def register(users, username, password):
    if username in users:
        return None
    else:
        user = User(username, password)
        users[username] = user
        return user

@app.route('/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = login(users, username, password)
    if user:
        token = generate_token(username)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/register', methods=['POST'])
def api_register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = register(users, username, password)
    if user:
        save_users(users)
        return jsonify({'message': f"Account for {username} created successfully!"})
    else:
        return jsonify({'message': 'Username already exists'}), 400
def get_user(username='houssam'):
    for user in users.values():
        if user.username == username:
            return user
    return None

@app.route('/recipes', methods=['GET'])
# @jwt_required()
@cross_origin()
def api_view_recipes():
    # current_user = get_jwt_identity()
    user = get_user()
    if user:
        try:
            return jsonify({'recipes': user.recipe_manager.view_recipes()})
        except Exception as e:
            print(f"Error fetching recipes: {e}")
            return jsonify({'message': 'Error fetching recipes'}), 500
    else:
        return jsonify({'message': 'User not found'}), 401



@app.route('/add_recipe', methods=['POST'])
# @jwt_required()
@cross_origin()
def api_add_recipe():
    current_user = get_user()
    if current_user:
        data = request.get_json()
        name = data.get('name')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if name and ingredients and instructions:
            message = current_user.recipe_manager.add_recipe(name, ingredients, instructions)
            return jsonify({'message': message})
        else:
            return jsonify({'message': 'Invalid data. Please provide name, ingredients, and instructions'}), 400
    else:
        return jsonify({'message': 'Login required'}), 401

@app.route('/search_recipes', methods=['GET'])
@jwt_required()
@cross_origin()
def api_search_recipes():
    if current_user:
        ingredient = request.args.get('ingredient')

        if ingredient:
            result = current_user.recipe_manager.search_recipes(ingredient)
            return jsonify({'result': result})
        else:
            return jsonify({'message': 'Invalid request. Please provide ingredient as a query parameter'}), 400
    else:
        return jsonify({'message': 'Login required'}), 401

@app.route('/delete_recipe', methods=['DELETE'])
@jwt_required()
@cross_origin()
def api_delete_recipe():
    if current_user:
        index = request.args.get('index')

        if index and index.isdigit():
            index = int(index)
            message = current_user.recipe_manager.delete_recipe(index)
            return jsonify({'message': message})
        else:
            return jsonify({'message': 'Invalid request. Please provide a valid index as a query parameter'}), 400
    else:
        return jsonify({'message': 'Login required'}), 401

@app.route('/update_recipe', methods=['PUT'])
@jwt_required()
@cross_origin()
def api_update_recipe():
    if current_user:
        data = request.get_json()
        index = data.get('index')
        name = data.get('name')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if index and index.isdigit() and name and ingredients and instructions:
            index = int(index)
            message = current_user.recipe_manager.update_recipe(index, name, ingredients, instructions)
            return jsonify({'message': message})
        else:
            return jsonify({'message': 'Invalid data. Please provide a valid index, name, ingredients, and instructions'}), 400
    else:
        return jsonify({'message': 'Login required'}), 401

if __name__ == '__main__':
    users = load_users()
    current_user = None
    app.run(debug=True)
