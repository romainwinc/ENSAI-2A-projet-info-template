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

    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS ingredients CASCADE
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
    )

    cursor.execute(
        sql.SQL(
            """
            CREATE TABLE {}.ingredients (
                id_ingredient SERIAL PRIMARY KEY,
                str_ingredient TEXT,
                str_description TEXT,
                str_type TEXT
                );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
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
