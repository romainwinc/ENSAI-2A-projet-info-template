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

try:

    conn = psycopg2.connect(
        dbname=POSTGRES_DATABASE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )

    cursor = conn.cursor()

    # Suppression si elle existe et Création de la table ingredients avec contrainte UNIQUE sur str_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredient CASCADE;
            CREATE TABLE {}.ingredient (
                id_ingredient SERIAL PRIMARY KEY,
                str_ingredient TEXT,
                str_description TEXT
                );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression si elle existe et Création de la table recettes avec contrainte UNIQUE sur str_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette CASCADE;
            CREATE TABLE {}.recette (
                id_recette SERIAL PRIMARY KEY,
                nom_recette TEXT NOT NULL,
                categorie TEXT,
                origine TEXT,
                instructions TEXT,
                mots_cles TEXT,
                url_image TEXT,
                liste_ingredients TEXT[],
                liste_mesures TEXT[],
                nombre_avis INT,
                note_moyenne FLOAT,
                date_derniere_modif DATE
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
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

# faire une table avec les id recettes et ingredients mesures
# faire une table avec idd recette et l 'idee de l'avias
# faire une table avec idée de l'avis et id de l'utilisateur

# ingredient1 TEXT,
# ingredient2 TEXT,
# ingredient3 TEXT,
# ingredient4 TEXT,
# ingredient5 TEXT,
# ingredient6 TEXT,
# ingredient7 TEXT,
# ingredient8 TEXT,
# ingredient9 TEXT,
# ingredient10 TEXT,
# ingredient11 TEXT,
# ingredient12 TEXT,
# ingredient13 TEXT,
# ingredient14 TEXT,
# ingredient15 TEXT,
# ingredient16 TEXT,
# ingredient17 TEXT,
# ingredient18 TEXT,
# ingredient19 TEXT,
# ingredient20 TEXT,
# mesure1 TEXT,
# mesure2 TEXT,
# mesure3 TEXT,
# mesure4 TEXT,
# mesure5 TEXT,
# mesure6 TEXT,
# mesure7 TEXT,
# mesure8 TEXT,
# mesure9 TEXT,
# mesure10 TEXT,
# mesure11 TEXT,
# mesure12 TEXT,
# mesure13 TEXT,
# mesure14 TEXT,
# mesure15 TEXT,
# mesure16 TEXT,
# mesure17 TEXT,
# mesure18 TEXT,
# mesure19 TEXT,
# mesure20 TEXT,
