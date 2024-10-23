from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class RecetteFavoriteDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_recette_favorite(self, id_recette, id_utilisateur):
        """Ajoute une recette aux favoris d'un utilisateur."""
        query = (
            """
            INSERT INTO {}.recette_favorite (id_recette, id_utilisateur)
            VALUES (%s, %s)
            """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))

    def get_favoris_by_user_id(self, id_utilisateur):
        """Récupère les noms des recettes favorites d'un utilisateur."""
        query = (
            """
            SELECT r.nom_recette 
            FROM {}.recette_favorite rf
            JOIN {}.recette r ON rf.id_recette = r.id_recette
            WHERE rf.id_utilisateur = %s
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return [row["nom_recette"] for row in cursor.fetchall()]

    def delete_recette_favorite(self, id_recette, id_utilisateur):
        """Supprime une recette des favoris d'un utilisateur."""
        query = (
            "DELETE FROM {}.recette_favorite WHERE id_recette = %s AND id_utilisateur = %s"
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))


if __name__ == "__main__":
    dao = RecetteFavoriteDAO()

    # Exemple d'utilisation :
    dao.add_recette_favorite(3, 1)  # Ajoute la recette 3 aux favoris de l'utilisateur 1
    print(dao.get_favoris_by_user_id(1))  # Renvoie les recettes favorites de l'utilisateur 1
    # dao.delete_recette_favorite(3, 1)  # Supprime la recette 3 des favoris de l'utilisateur 1
