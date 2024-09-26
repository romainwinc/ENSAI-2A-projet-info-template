# Création de la table 

CREATE TABLE IF NOT EXISTS ingredients (
    id SERIAL PRIMARY KEY,
    ingredient_id VARCHAR(255),
    ingredient_name VARCHAR(255),
    description TEXT,
    ingredient_type VARCHAR(255)
);

# ReRemplissage de la table

import requests
import psycopg2

class Ingredient:
    def __init__(self, idIngredient, strIngredient, strDescription, strType):
        self.idIngredient = idIngredient
        self.strIngredient = strIngredient
        self.strDescription = strDescription
        self.strType = strType

    def __repr__(self):
        return (
            f"Ingredient: {self.strIngredient}\n"
            f"Description: {self.strDescription if self.strDescription else 'Aucune'}\n"
            f"Type: {self.strType if self.strType else 'Inconnu'}\n"
        )


def get_ingredients_from_api():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?i=list'
    response = requests.get(url)
    ingredients_data = response.json()

    ingredients = []
    if ingredients_data['meals'] is not None:
        for ingredient_data in ingredients_data['meals']:
            ingredient = Ingredient(
                ingredient_data['idIngredient'],
                ingredient_data['strIngredient'],
                ingredient_data.get('strDescription'),
                ingredient_data.get('strType')
            )
            ingredients.append(ingredient)

    return ingredients


def insert_ingredients_into_db(ingredients):
    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        host="localhost",        # Remplacez par votre hôte
        database="your_database",  # Remplacez par votre nom de base de données
        user="your_user",         # Remplacez par votre utilisateur PostgreSQL
        password="your_password"  # Remplacez par votre mot de passe
    )
    cur = conn.cursor()

    # Insertion des ingrédients dans la table PostgreSQL
    for ingredient in ingredients:
        insert_query = '''
            INSERT INTO ingredients (
                ingredient_id, ingredient_name, description, ingredient_type
            ) VALUES (%s, %s, %s, %s)
        '''
        cur.execute(insert_query, (
            ingredient.idIngredient, ingredient.strIngredient,
            ingredient.strDescription, ingredient.strType
        ))

    # Commit et fermeture de la connexion
    conn.commit()
    cur.close()
    conn.close()

    print("Tous les ingrédients ont été insérés dans la base de données.")


# Extraction des ingrédients et insertion dans la base de données
ingredients = get_ingredients_from_api()
insert_ingredients_into_db(ingredients)
