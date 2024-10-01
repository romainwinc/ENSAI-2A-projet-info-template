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
    # avec contrainte UNIQUE sur str_ingredient
    cursor.execute(
        sql.SQL(
            """
            DROP TABLE IF EXISTS {}.ingredient CASCADE;
            CREATE TABLE {}.ingredient (
                id_ingredient SERIAL PRIMARY KEY,
                nom_ingredient VARCHAR(255) UNIQUE,
                description_ingredient VARCHAR(255)
            );
            """
        ).format(sql.Identifier(POSTGRES_SCHEMA))
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
                instructions TEXT,  -- Texte complet pour les instructions
                mots_cles VARCHAR(255),
                url_image VARCHAR(255),
                liste_ingredients JSONB,  -- Stocker une liste de dictionnaires en JSONB
                nombre_avis INT,
                note_moyenne FLOAT,
                date_derniere_modif DATE
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


# try:
#     conn = psycopg2.connect(
#         dbname=POSTGRES_DATABASE,
#         user=POSTGRES_USER,
#         password=POSTGRES_PASSWORD,
#         host=POSTGRES_HOST,
#         port=POSTGRES_PORT,
#     )

#     cursor = conn.cursor()

#     # Suppression si elle existe et Création de la table utilisateur avec historique en JSONB
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.utilisateur CASCADE;
#             CREATE TABLE {}.utilisateur (
#                 id_utilisateur SERIAL PRIMARY KEY,
#                 nom_utilisateur VARCHAR(255),
#                 mot_de_passe VARCHAR(255),
#                 date_inscription DATE,
#                 historique JSONB,  -- Stocker une liste de consultations en JSONB
#                 recettes_favorites INT[] REFERENCES {}.recette(id_recette),
#                 ingredients_favoris INT[] REFERENCES {}.ingredient(id_ingredient),
#                 ingredients_non_desires INT[] REFERENCES {}.ingredient(id_ingredient),
#                 liste_de_courses INT[] REFERENCES {}.ingredient(id_ingredient)
#             );
#             """
#         ).format(
#             sql.Identifier(POSTGRES_SCHEMA),
#             sql.Identifier(POSTGRES_SCHEMA),
#             sql.Identifier(POSTGRES_SCHEMA),
#             sql.Identifier(POSTGRES_SCHEMA),
#         )
#     )

#     # Suppression si elle existe et Création de la table avis
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.avis CASCADE;
#             CREATE TABLE {}.avis (
#                 id_avis SERIAL PRIMARY KEY,
#                 titre_avis VARCHAR(255),
#                 nom_auteur VARCHAR(255),
#                 date_publication DATE,
#                 commentaire TEXT,  -- Texte complet pour le commentaire
#                 note INT
#             );
#             """
#         ).format(sql.Identifier(POSTGRES_SCHEMA))
#     )

#     # Suppression si elle existe et Création de la table demande
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.demande CASCADE;
#             CREATE TABLE {}.demande (
#                 id_demande SERIAL PRIMARY KEY,
#                 id_utilisateur INT,
#                 type_demande VARCHAR(255), -- Modification ou Suppression
#                 attribut_modifie VARCHAR(255),
#                 attribut_corrige VARCHAR(255),
#                 commentaire_demande TEXT  -- Texte complet pour le commentaire de la demande
#             );
#             """
#         ).format(sql.Identifier(POSTGRES_SCHEMA))
#     )

#     # Suppression si elle existe et Création de la table utilisateur_avis (relation utilisateur-avis)
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.utilisateur_avis CASCADE;
#             CREATE TABLE {}.utilisateur_avis (
#                 id_utilisateur INT REFERENCES {}.utilisateur(id_utilisateur),
#                 id_avis INT REFERENCES {}.avis(id_avis),
#                 PRIMARY KEY (id_utilisateur, id_avis)
#             );
#             """
#         ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
#     )

#     # Suppression si elle existe et Création de la table recette_avis (relation recette-avis)
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.recette_avis CASCADE;
#             CREATE TABLE {}.recette_avis (
#                 id_recette INT REFERENCES {}.recette(id_recette),
#                 id_avis INT REFERENCES {}.avis(id_avis),
#                 PRIMARY KEY (id_recette, id_avis)
#             );
#             """
#         ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
#     )

#     # Suppression si elle existe et Création de la table consultation (historique des consultations)
#     cursor.execute(
#         sql.SQL(
#             """
#             DROP TABLE IF EXISTS {}.consultation CASCADE;
#             CREATE TABLE {}.consultation (
#                 id_recette INT REFERENCES {}.recette(id_recette),
#                 id_utilisateur INT REFERENCES {}.utilisateur(id_utilisateur),
#                 date_consultation DATE,
#                 PRIMARY KEY (id_recette, id_utilisateur)
#             );
#             """
#         ).format(sql.Identifier(POSTGRES_SCHEMA), sql.Identifier(POSTGRES_SCHEMA))
#     )

# # Valider les modifications
#     conn.commit()

# except Exception as e:
#     print(f"Erreur lors de la connexion ou de l'exécution des requêtes : {e}")

# finally:
#     # Fermer la connexion
#     if cursor:
#         cursor.close()
#     if conn:
#         conn.close()
