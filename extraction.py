# Remplissage de la table en utilisant l'API

import requests
import psycopg2


def get_recipes_from_api():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    recettes = []

    for letter in alphabet:
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        response = requests.get(url)
        meals_data = response.json()

        if meals_data["meals"] is not None:
            for meal in meals_data["meals"]:
                ingredients = [meal.get(f"strIngredient{i}") for i in range(1, 21)]
                measures = [meal.get(f"strMeasure{i}") for i in range(1, 21)]

                recette = Recette(
                    meal["idMeal"],
                    meal["strMeal"],
                    meal["strCategory"],
                    meal["strArea"],
                    meal["strInstructions"],
                    meal.get("strTags"),
                    ingredients,
                    measures,
                )
                recettes.append(recette)

    return recettes


def insert_recipes_into_db(recettes):
    # Connexion à la base de données PostgreSQL
    conn = psycopg2.connect(
        host="localhost",  # Remplacez par votre hôte
        database="your_database",  # Remplacez par votre nom de base de données
        user="your_user",  # Remplacez par votre utilisateur PostgreSQL
        password="your_password",  # Remplacez par votre mot de passe
    )
    cur = conn.cursor()

    # Insertion des recettes dans la table PostgreSQL
    for recette in recettes:
        insert_query = """
            INSERT INTO recipes (
                meal_id, meal_name, category, area, instructions, tags, ingredient1, ingredient2, ingredient3,
                ingredient4, ingredient5, ingredient6, ingredient7, ingredient8, ingredient9, ingredient10,
                ingredient11, ingredient12, ingredient13, ingredient14, ingredient15, ingredient16, ingredient17,
                ingredient18, ingredient19, ingredient20, measure1, measure2, measure3, measure4, measure5, measure6,
                measure7, measure8, measure9, measure10, measure11, measure12, measure13, measure14, measure15,
                measure16, measure17, measure18, measure19, measure20
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(
            insert_query,
            (
                recette.idMeal,
                recette.strMeal,
                recette.strCategory,
                recette.strArea,
                recette.strInstructions,
                recette.strTags,
                *recette.ingredients,
                *recette.measures,
            ),
        )

    # Commit et fermeture de la connexion
    conn.commit()
    cur.close()
    conn.close()

    print("Toutes les recettes ont été insérées dans la base de données.")


# Extraction des recettes et insertion dans la base de données
recettes = get_recipes_from_api()
insert_recipes_into_db(recettes)
