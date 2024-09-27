import os
import dotenv
import requests
import pandas as pd
import psycopg2
from psycopg2 import sql

# Variables d'environnement

dotenv.load_dotenv()
WEBSERVICE_HOST = os.getenv("WEBSERVICE_HOST")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA")


# Vérification si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire les informations des ingrédients
    ingredients = data.get("meals", [])

    # Créer une DataFrame avec les informations importantes
    df = pd.DataFrame(ingredients)

    # Connexion à la base de données PostgreSQL
    # Connexion à la base de données PostgreSQL

    cursor = None

    try:

        conn = psycopg2.connect(
            dbname=POSTGRES_DATABASE,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
        )
        cursor = conn.cursor()

        # Insérer les données dans la table en précisant le schéma
        for _, row in df.iterrows():
            cursor.execute(
                sql.SQL(
                    """
                    INSERT INTO {}.ingredients (id_ingredient, str_ingredient, str_description, str_type)
                    VALUES (%s, %s, %s, %s)
                    """
                ).format(sql.Identifier(POSTGRES_SCHEMA)),
                (
                    row.get("idIngredient"),
                    row.get("strIngredient"),
                    row.get("strDescription"),
                    row.get("strType"),
                ),
            )

        # Valider les modifications
        conn.commit()

    except Exception as e:
        print(f"Erreur lors de la connexion ou de l'exécution des requêtes : {e}")

    finally:
        # Fermer la connexion
        if cursor:
            cursor.close()
        if conn:
            conn.close()

else:
    print("Erreur lors de la récupération des données depuis l'API")
