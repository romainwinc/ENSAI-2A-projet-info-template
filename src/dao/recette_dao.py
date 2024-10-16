from dao.db_connection import DBConnection
from utils.singleton import Singleton


class RecetteDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def get_all_recettes(self):
        """Récupère toutes les recettes de la table 'recette'."""
        query = """
            SELECT id_recette, nom_recette, categorie, origine, instructions, 
                   mots_cles, url_image, liste_ingredients, nombre_avis, 
                   note_moyenne, date_derniere_modif
            FROM recette
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

        recettes = []
        for row in rows:
            recette = {
                "id_recette": row[0],
                "nom_recette": row[1],
                "categorie": row[2],
                "origine": row[3],
                "instructions": row[4],
                "mots_cles": row[5],
                "url_image": row[6],
                "liste_ingredients": row[7],
                "nombre_avis": row[8],
                "note_moyenne": row[9],
                "date_derniere_modif": row[10],
            }
            recettes.append(recette)

        return recettes

    def get_recette_by_id(self, recette_id):
        """Récupère une recette spécifique par son ID."""
        query = """
            SELECT id_recette, nom_recette, categorie, origine, instructions, 
                   mots_cles, url_image, liste_ingredients, nombre_avis, 
                   note_moyenne, date_derniere_modif
            FROM recette
            WHERE id_recette = %s
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))
                row = cursor.fetchone()

        if row:
            recette = {
                "id_recette": row[0],
                "nom_recette": row[1],
                "categorie": row[2],
                "origine": row[3],
                "instructions": row[4],
                "mots_cles": row[5],
                "url_image": row[6],
                "liste_ingredients": row[7],
                "nombre_avis": row[8],
                "note_moyenne": row[9],
                "date_derniere_modif": row[10],
            }
            return recette
        return None

    def add_recette(
        self,
        nom_recette,
        categorie,
        origine,
        instructions,
        mots_cles,
        url_image,
        liste_ingredients,
        nombre_avis,
        note_moyenne,
        date_derniere_modif,
    ):
        """Ajoute une nouvelle recette dans la table 'recette'."""
        query = """
            INSERT INTO recette (nom_recette, categorie, origine, instructions, 
                                 mots_cles, url_image, liste_ingredients, nombre_avis, 
                                 note_moyenne, date_derniere_modif)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id_recette
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        nom_recette,
                        categorie,
                        origine,
                        instructions,
                        mots_cles,
                        url_image,
                        liste_ingredients,
                        nombre_avis,
                        note_moyenne,
                        date_derniere_modif,
                    ),
                )
                recette_id = cursor.fetchone()[0]
        return recette_id

    def update_recette(self, recette_id, **kwargs):
        """Met à jour une recette existante."""
        query = "UPDATE recette SET "
        query += ", ".join([f"{key} = %s" for key in kwargs])
        query += " WHERE id_recette = %s"

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), recette_id))

    def delete_recette(self, recette_id):
        """Supprime une recette par son ID."""
        query = "DELETE FROM recette WHERE id_recette = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (recette_id,))
