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

    # Suppression si elle existe et Création de la table ingredients
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredient CASCADE;
            CREATE TABLE {}.ingredient (
                id_ingredient SERIAL PRIMARY KEY,
                nom_ingredient VARCHAR(255) UNIQUE,
                description_ingredient TEXT
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
    )

    # Suppression si elle existe et Création de la table recettes
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette CASCADE;
            CREATE TABLE {}.recette (
                id_recette SERIAL PRIMARY KEY,
                nom_recette VARCHAR(255) NOT NULL,
                categorie VARCHAR(255),
                origine VARCHAR(255),
                instructions TEXT,
                mots_cles VARCHAR(255),
                url_image VARCHAR(255),
                liste_ingredients VARCHAR(255)[],
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


try:
    conn = psycopg2.connect(
        dbname=POSTGRES_DATABASE,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )

    cursor = conn.cursor()

    # Suppression si elle existe et Création de la table utilisateur avec historique en JSONB
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.utilisateur CASCADE;
            CREATE TABLE {}.utilisateur (
                id_utilisateur SERIAL PRIMARY KEY,
                nom_utilisateur VARCHAR(255),
                mot_de_passe VARCHAR(255),
                role VARCHAR(255),
                date_inscription DATE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression si elle existe et Création de la table avis
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.avis CASCADE;
            CREATE TABLE {}.avis (
                id_avis SERIAL PRIMARY KEY,
                id_recette INT REFERENCES {}.recette(id_recette) ON DELETE CASCADE,
                id_utilisateur INT REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE,
                titre_avis VARCHAR(255),
                nom_auteur VARCHAR(255),
                date_publication DATE,
                commentaire TEXT,
                note INT
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression si elle existe et Création de la table demande
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.demande CASCADE;
            CREATE TABLE {}.demande (
                id_demande SERIAL PRIMARY KEY,
                id_utilisateur INT,
                type_demande VARCHAR(255),
                attribut_modifie VARCHAR(255),
                attribut_corrige VARCHAR(255),
                commentaire_demande TEXT,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression si elle existe et Création de la table consultation (historique des consultations)
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.consultation CASCADE;
            CREATE TABLE {}.consultation (
                id_recette INT,
                id_utilisateur INT,
                date_consultation DATE,
                PRIMARY KEY (id_recette, id_utilisateur),
                FOREIGN KEY (id_recette) REFERENCES {}.recette(id_recette) ON DELETE CASCADE,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression si elle existe et Création de la recette_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette_ingredient CASCADE;
            CREATE TABLE {}.recette_ingredient (
                id_recette INT,
                id_ingredient INT,
                mesure VARCHAR(255),
                PRIMARY KEY (id_recette, id_ingredient),
                FOREIGN KEY (id_recette) REFERENCES {}.recette(id_recette) ON DELETE CASCADE,
                FOREIGN KEY (id_ingredient) REFERENCES {}.ingredient(id_ingredient) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    # Suppression si elle existe et Création de la recette_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.recette_favorite CASCADE;
            CREATE TABLE {}.recette_favorite (
                id_recette INT,
                id_utilisateur INT,
                PRIMARY KEY (id_recette, id_utilisateur),
                FOREIGN KEY (id_recette) REFERENCES {}.recette(id_recette) ON DELETE CASCADE,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredients_favoris CASCADE;
            CREATE TABLE {}.ingredients_favoris (
                id_ingredient INT,
                id_utilisateur INT,
                PRIMARY KEY (id_ingredient, id_utilisateur),
                FOREIGN KEY (id_ingredient) REFERENCES {}.ingredient(id_ingredient) ON DELETE CASCADE,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredients_non_desires CASCADE;
            CREATE TABLE {}.ingredients_non_desires (
                id_ingredient INT,
                id_utilisateur INT,
                PRIMARY KEY (id_ingredient, id_utilisateur),
                FOREIGN KEY (id_ingredient) REFERENCES {}.ingredient(id_ingredient) ON DELETE CASCADE,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
    )

    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.liste_de_courses CASCADE;
            CREATE TABLE {}.liste_de_courses (
                id_ingredient INT,
                id_recette INT,
                id_utilisateur INT,
                PRIMARY KEY (id_ingredient, id_recette, id_utilisateur),
                FOREIGN KEY (id_ingredient, id_recette) REFERENCES {}.recette_ingredient(id_ingredient, id_recette) ON DELETE CASCADE,
                FOREIGN KEY (id_utilisateur) REFERENCES {}.utilisateur(id_utilisateur) ON DELETE CASCADE
            );
            """
        ).format(
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
            sql.Identifier(POSTGRES_SCHEMA),
        )
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
