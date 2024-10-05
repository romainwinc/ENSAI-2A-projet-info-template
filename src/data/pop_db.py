import os
import dotenv
import requests
import pandas as pd
from datetime import date
import psycopg2
from psycopg2 import sql

# Charger les variables d'environnement
dotenv.load_dotenv()
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA")

# Récupération des ingrédients
url_ingredients = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
response_ingredients = requests.get(url_ingredients)

if response_ingredients.status_code == 200:
    data_ingredients = response_ingredients.json()
    ingredients = data_ingredients.get("meals", [])

    # Créer une DataFrame avec les informations des ingrédients
    df_ingredients = pd.DataFrame(ingredients)

    try:
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            dbname=POSTGRES_DATABASE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        cursor = conn.cursor()

        # S'assurer que le schéma est correctement sélectionné
        cursor.execute(sql.SQL("SET search_path TO {};").format(sql.Identifier(POSTGRES_SCHEMA)))

        # Insérer les données dans la table des ingrédients
        for _, row in df_ingredients.iterrows():
            cursor.execute(
                sql.SQL(
                    """
                    INSERT INTO {}.ingredient (id_ingredient, nom_ingredient, description_ingredient)
                    VALUES (%s, %s, %s)
                    """
                ).format(sql.Identifier(POSTGRES_SCHEMA)),
                (row.get("idIngredient"), row.get("strIngredient"), row.get("strDescription")),
            )

        # Valider les modifications
        conn.commit()

    except Exception as e:
        print(
            f"Erreur lors de la connexion ou de l'exécution des requêtes pour les ingrédients : {e}"
        )

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

else:
    print("Erreur lors de la récupération des données depuis l'API des ingrédients")

# Récupération des recettes

try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DATABASE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )
    cursor = conn.cursor()

    # S'assurer que le schéma est correctement sélectionné
    cursor.execute(sql.SQL("SET search_path TO {};").format(sql.Identifier(POSTGRES_SCHEMA)))

    # Boucle sur toutes les lettres de l'alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        url_recette = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
        response_recette = requests.get(url_recette)

        if response_recette.status_code == 200:
            data_recette = response_recette.json()
            recettes = data_recette.get("meals", [])

            if not recettes:
                print(f"Aucune recette trouvée pour la lettre {letter}")
                continue

            # Créer une DataFrame avec les informations des recettes
            df_recettes = pd.DataFrame(recettes)

            # Insérer les données dans la table recette
            for _, row in df_recettes.iterrows():
                ingredients = []

                # Extraire les ingrédients et les quantités
                for i in range(1, 21):
                    ingredient = row.get(f"strIngredient{i}")
                    measure = row.get(f"strMeasure{i}")

                    if ingredient:  # Si l'ingrédient est présent
                        ingredients.append({ingredient: measure})

                cursor.execute(
                    sql.SQL(
                        """
                        INSERT INTO {}.recette (
                            nom_recette, categorie, origine, instructions, mots_cles,
                            url_image, liste_ingredients, nombre_avis,
                            note_moyenne, date_derniere_modif
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                    ).format(sql.Identifier(POSTGRES_SCHEMA)),
                    (
                        row.get("strMeal"),  # nom_recette
                        row.get("strCategory"),  # categorie
                        row.get("strArea"),  # origine
                        row.get("strInstructions"),  # instructions
                        row.get("strTags"),  # mots_cles
                        row.get("strMealThumb"),  # url_image
                        ingredients,  # liste_ingredients en JSON
                        0,  # nombre_avis (initialisé à 0)
                        None,  # note_moyenne (aucune note pour l'instant)
                        date.today(),  # date_derniere_modif
                    ),
                )

            # Valider les modifications pour cette lettre
            conn.commit()

        else:
            print(
                f"Erreur lors de la récupération des données depuis l'API pour la lettre {letter}"
            )

except Exception as e:
    print(f"Erreur lors de la connexion ou de l'exécution des requêtes pour les recettes : {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
