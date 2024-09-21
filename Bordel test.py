import os
import requests
import pandas as pd
import psycopg2
from psycopg2 import sql

# Variables d'environnement
WEBSERVICE_HOST = os.getenv("WEBSERVICE_HOST", "https://pokeapi.co/api/v2")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "sgbd-eleves.domensai.ecole")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE", "id2501")
POSTGRES_USER = os.getenv("POSTGRES_USER", "id2501")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "id2501")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA", "projet")

# URL de l'API
url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
response = requests.get(url)

# Vérification si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire les informations des ingrédients
    ingredients = data.get("meals", [])

    # Créer une DataFrame avec les informations importantes
    df = pd.DataFrame(ingredients)

    # Connexion à la base de données PostgreSQL
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

        # Création de la table ingredients dans le schéma spécifié
        cursor.execute(
            sql.SQL(
                """
                CREATE TABLE IF NOT EXISTS {}.ingredients (
                    idIngredient SERIAL PRIMARY KEY,
                    strIngredient TEXT,
                    strDescription TEXT,
                    strType TEXT
                );
            """
            ).format(sql.Identifier(POSTGRES_SCHEMA))
        )

        # Insérer les données dans la table en précisant le schéma
        for _, row in df.iterrows():
            cursor.execute(
                sql.SQL(
                    """
                    INSERT INTO {}.ingredients (strIngredient, strDescription, strType)
                    VALUES (%s, %s, %s)
                    ON CONFLICT DO NOTHING;
                """
                ).format(sql.Identifier(POSTGRES_SCHEMA)),
                (row.get("strIngredient"), row.get("strDescription"), row.get("strType")),
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
