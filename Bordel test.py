import requests
import pandas as pd
import psycopg2

# URL de l'API
url = "https://www.themealdb.com/api/json/v1/1/list.php?i=list"
response = requests.get(url)

# Vérification si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Extraire les informations des ingrédients
    ingredients = data["meals"]

    # Créer une DataFrame avec les informations importantes
    df = pd.DataFrame(ingredients)

    # Connexion à la base de données PostgreSQL
    try:
        conn = psycopg2.connect(
            dbname="votre_base_de_donnees",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            host="localhost",  # ou l'adresse IP de votre serveur PostgreSQL
            port="5432",
        )
        cursor = conn.cursor()

        # Création de la table ingredients
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS ingredients (
                idIngredient SERIAL PRIMARY KEY,
                strIngredient TEXT,
                strDescription TEXT,
                strType TEXT
            )
        """
        )

        # Insérer les données dans la table
        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO ingredients (idIngredient, strIngredient, strDescription, strType)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (idIngredient) DO NOTHING
            """,
                (row["idIngredient"], row["strIngredient"], row["strDescription"], row["strType"]),
            )

        # Valider les modifications
        conn.commit()

    except Exception as e:
        print(f"Erreur lors de la connexion ou de l'exécution des requêtes : {e}")

    finally:
        # Fermer la connexion
        cursor.close()
        conn.close()

else:
    print("Erreur lors de la récupération des données depuis l'API")
