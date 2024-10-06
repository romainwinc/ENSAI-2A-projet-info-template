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

# # Récupération des ingrédients
# url_ingredients = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
# response_ingredients = requests.get(url_ingredients)

# if response_ingredients.status_code == 200:
#     data_ingredients = response_ingredients.json()
#     ingredients = data_ingredients.get("meals", [])

#     # Créer une DataFrame avec les informations des ingrédients
#     df_ingredients = pd.DataFrame(ingredients)

#     try:
#         # Connexion à la base de données PostgreSQL
#         conn = psycopg2.connect(
#             dbname=POSTGRES_DATABASE,
#             user=POSTGRES_USER,
#             password=POSTGRES_PASSWORD,
#             host=POSTGRES_HOST,
#             port=POSTGRES_PORT,
#         )
#         cursor = conn.cursor()

#         # S'assurer que le schéma est correctement sélectionné
#         cursor.execute(sql.SQL("SET search_path TO {};").format(sql.Identifier(POSTGRES_SCHEMA)))

#         # Insérer les données dans la table des ingrédients
#         for _, row in df_ingredients.iterrows():
#             cursor.execute(
#                 sql.SQL(
#                     """
#                     INSERT INTO {}.ingredient (id_ingredient, nom_ingredient, description_ingredient)
#                     VALUES (%s, %s, %s)
#                     """
#                 ).format(sql.Identifier(POSTGRES_SCHEMA)),
#                 (row.get("idIngredient"), row.get("strIngredient"), row.get("strDescription")),
#             )

#         # Valider les modifications
#         conn.commit()

#     except Exception as e:
#         print(
#             f"Erreur lors de la connexion ou de l'exécution des requêtes pour les ingrédients : {e}"
#         )

#     finally:
#         if cursor:
#             cursor.close()
#         if conn:
#             conn.close()

# else:
#     print("Erreur lors de la récupération des données depuis l'API des ingrédients")

# # Récupération des recettes

# # Connexion à la base de données
# try:
#     conn = psycopg2.connect(
#         dbname=POSTGRES_DATABASE,
#         user=POSTGRES_USER,
#         password=POSTGRES_PASSWORD,
#         host=POSTGRES_HOST,
#         port=POSTGRES_PORT,
#     )
#     cursor = conn.cursor()

#     # S'assurer que le schéma est correctement sélectionné
#     cursor.execute(sql.SQL("SET search_path TO {};").format(sql.Identifier(POSTGRES_SCHEMA)))

#     # Boucle sur toutes les lettres de l'alphabet
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for letter in alphabet:
#         url_recette = f"https://www.themealdb.com/api/json/v1/1/search.php?f={letter}"
#         response_recette = requests.get(url_recette)

#         if response_recette.status_code == 200:
#             data_recette = response_recette.json()
#             recettes = data_recette.get("meals", [])

#             if not recettes:
#                 print(f"Aucune recette trouvée pour la lettre {letter}")
#                 continue

#             # Créer une DataFrame avec les informations des recettes
#             df_recettes = pd.DataFrame(recettes)

#             # Insérer les données dans la table recette
#             for _, row in df_recettes.iterrows():
#                 ingredients = []

#                 # Extraire uniquement les ingrédients
#                 for i in range(1, 21):
#                     ingredient = row.get(f"strIngredient{i}")

#                     if ingredient:  # Si l'ingrédient est présent
#                         ingredients.append(ingredient)  # Ajoute uniquement l'ingrédient

#                 # Insertion dans la table recette
#                 cursor.execute(
#                     sql.SQL(
#                         """
#                         INSERT INTO {}.recette (
#                             nom_recette, categorie, origine, instructions, mots_cles,
#                             url_image, liste_ingredients, nombre_avis,
#                             note_moyenne, date_derniere_modif
#                         )
#                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#                         """
#                     ).format(sql.Identifier(POSTGRES_SCHEMA)),
#                     (
#                         row.get("strMeal"),  # nom_recette
#                         row.get("strCategory"),  # categorie
#                         row.get("strArea"),  # origine
#                         row.get("strInstructions"),  # instructions
#                         row.get("strTags"),  # mots_cles
#                         row.get("strMealThumb"),  # url_image
#                         ingredients,  # liste_ingredients sans mesure
#                         0,  # nombre_avis (initialisé à 0)
#                         None,  # note_moyenne (aucune note pour l'instant)
#                         date.today(),  # date_derniere_modif
#                     ),
#                 )

#             # Valider les modifications pour cette lettre
#             conn.commit()

#         else:
#             print(
#                 f"Erreur lors de la récupération des données depuis l'API pour la lettre {letter}"
#             )

# except Exception as e:
#     print(f"Erreur lors de la connexion ou de l'exécution des requêtes pour les recettes : {e}")

# finally:
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()

# # Création de la table de jointure entre recettes et ingrédients
# cursor.execute(
#     sql.SQL(
#         """
#         DROP TABLE IF EXISTS {}.recette_ingredient CASCADE;
#         CREATE TABLE {}.recette_ingredient (
#             id_recette INT,
#             id_ingredient INT,
#             mesure VARCHAR(255),
#             PRIMARY KEY (id_recette, id_ingredient),
#             FOREIGN KEY (id_recette) REFERENCES {}.recette(id_recette) ON DELETE CASCADE,
#             FOREIGN KEY (id_ingredient) REFERENCES {}.ingredient(id_ingredient) ON DELETE CASCADE
#         );
#         """
#     ).format(
#         sql.Identifier(POSTGRES_SCHEMA),
#         sql.Identifier(POSTGRES_SCHEMA),
#         sql.Identifier(POSTGRES_SCHEMA),
#         sql.Identifier(POSTGRES_SCHEMA),
#     )
# )

# Insérer les données dans la table de jointure recette_ingredient
try:

    conn = psycopg2.connect(
        dbname=POSTGRES_DATABASE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )
    cursor = conn.cursor()

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

            for recette in recettes:
                nom_recette = recette.get("strMeal")

                # Récupérer l'ID de la recette insérée
                cursor.execute(
                    sql.SQL("SELECT id_recette FROM {}.recette WHERE nom_recette = %s").format(
                        sql.Identifier(POSTGRES_SCHEMA)
                    ),
                    (nom_recette,),
                )
                id_recette = cursor.fetchone()[0]

                # Traiter les ingrédients et mesures
                for i in range(1, 21):
                    ingredient_name = recette.get(f"strIngredient{i}")
                    measure = recette.get(f"strMeasure{i}")

                    if ingredient_name:  # Si un ingrédient est présent
                        # Récupérer l'ID de l'ingrédient
                        cursor.execute(
                            sql.SQL(
                                "SELECT id_ingredient FROM {}.ingredient WHERE nom_ingredient = %s"
                            ).format(sql.Identifier(POSTGRES_SCHEMA)),
                            (ingredient_name,),
                        )
                        result = cursor.fetchone()

                        if result:
                            id_ingredient = result[0]

                            # Insérer dans la table recette_ingredient
                            cursor.execute(
                                sql.SQL(
                                    """
                                    INSERT INTO {}.recette_ingredient (id_recette, id_ingredient, mesure)
                                    VALUES (%s, %s, %s)
                                    """
                                ).format(sql.Identifier(POSTGRES_SCHEMA)),
                                (id_recette, id_ingredient, measure),
                            )

            # Valider les modifications pour cette lettre
            conn.commit()

        else:
            print(
                f"Erreur lors de la récupération des données depuis l'API pour la lettre {letter}"
            )

except Exception as e:
    print(f"Erreur lors de l'insertion dans la table recette_ingredient : {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
