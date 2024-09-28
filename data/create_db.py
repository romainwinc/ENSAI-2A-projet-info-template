import os
import dotenv
import psycopg2
from psycopg2 import sql
import json  # Import nécessaire pour manipuler les données JSON

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

    # Suppression de la table "ingredient" si elle existe
    # et création avec une contrainte UNIQUE sur str_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredient CASCADE;
            CREATE TABLE {}.ingredient (
                id_ingredient SERIAL PRIMARY KEY,
                str_ingredient TEXT UNIQUE,
                str_description TEXT
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "recette" si elle existe et création
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
                liste_ingredients INT[] REFERENCES {}.ingredient(id_ingredient),
                liste_mesures TEXT[],
                nombre_avis INT,
                note_moyenne FLOAT,
                date_derniere_modif DATE
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "utilisateur" si elle existe
    # et création avec un champ historique de type JSONB
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.utilisateur CASCADE;
            CREATE TABLE {}.utilisateur (
                id_utilisateur SERIAL PRIMARY KEY,
                nom_utilisateur TEXT,
                mot_de_passe TEXT,
                date_inscription DATE,
                historique JSONB,  -- Stocker l'historique des consultations sous forme JSONB
                recettes_favorites INT[] REFERENCES {}.recette(id_recette),
                ingredients_favoris INT[] REFERENCES {}.ingredient(id_ingredient),
                ingredients_non_desires INT[] REFERENCES {}.ingredient(id_ingredient),
                liste_de_courses INT[] REFERENCES {}.ingredient(id_ingredient)
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression de la table "avis" si elle existe et création
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.avis CASCADE;
            CREATE TABLE {}.avis (
                id_avis SERIAL PRIMARY KEY,
                titre_avis TEXT,
                nom_auteur TEXT,
                date_publication DATE,
                commentaire TEXT,
                note INT
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "utilisateur_avis" si elle existe
    # et création (relation utilisateur-avis)
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.utilisateur_avis CASCADE;
            CREATE TABLE {}.utilisateur_avis (
                id_utilisateur INT REFERENCES {}.utilisateur(id_utilisateur),
                id_avis INT REFERENCES {}.avis(id_avis),
                PRIMARY KEY (id_utilisateur, id_avis)
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "recette_avis" si elle existe
    #  et création (relation recette-avis)
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette_avis CASCADE;
            CREATE TABLE {}.recette_avis (
                id_recette INT REFERENCES {}.recette(id_recette),
                id_avis INT REFERENCES {}.avis(id_avis),
                PRIMARY KEY (id_recette, id_avis)
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "recette_ingredient" si elle existe
    #  et création (relation recette-ingredient)
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette_ingredient CASCADE;
            CREATE TABLE {}.recette_ingredient (
                id_recette INT REFERENCES {}.recette(id_recette),
                id_ingredient INT REFERENCES {}.avis(id_ingredient),
                quantite TEXT,
                PRIMARY KEY (id_recette, id_ingredient)
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression de la table "consultation" si elle existe
    # et création pour stocker l'historique des consultations
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.consultation CASCADE;
            CREATE TABLE {}.consultation (
                id_recette INT REFERENCES {}.recette(id_recette),
                id_utilisateur INT REFERENCES {}.utilisateur(id_utilisateur),
                date_consultation DATE,
                PRIMARY KEY (id_recette, id_utilisateur, date_consultation)
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Valider les modifications dans la base de données
    conn.commit()

except Exception as e:
    print(f"Erreur lors de la connexion ou de l'exécution des requêtes : {e}")

finally:
    # Fermer le curseur et la connexion
    if cursor:
        cursor.close()
    if conn:
        conn.close()
