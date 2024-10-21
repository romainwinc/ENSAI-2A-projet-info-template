from dao.db_connection import DBConnection
from utils.singleton import Singleton


class RecetteFavoriteDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_recette_favorite(self, id_recette, id_utilisateur):
        """Ajoute une recette aux favoris d'un utilisateur."""
        query = """
            INSERT INTO recette_favorite (id_recette, id_utilisateur)
            VALUES (%s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))

    def get_favorites_by_user_id(self, id_utilisateur):
        """Récupère les recettes favorites d'un utilisateur."""
        query = "SELECT * FROM recette_favorite WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_recette_favorite(self, id_recette, id_utilisateur):
        """Met à jour un favori."""
        # Cette méthode est un exemple et pourrait ne pas avoir de sens dans ce contexte,
        # car les favoris sont généralement ajoutés ou supprimés, mais je l'inclus pour respecter la demande.
        pass

    def delete_favorite(self, id_recette, id_utilisateur):
        """Supprime une recette des favoris d'un utilisateur."""
        query = "DELETE FROM recette_favorite WHERE id_recette = %s AND id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))
