from dao.db_connection import DBConnection
from utils.singleton import Singleton


class IngredientsFavorisDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_ingredient_favori(self, id_ingredient, id_utilisateur):
        """Ajoute un ingrédient aux favoris d'un utilisateur."""
        query = """
            INSERT INTO ingredients_favoris (id_ingredient, id_utilisateur)
            VALUES (%s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))

    def get_favoris_by_user_id(self, id_utilisateur):
        """Récupère les ingrédients favoris d'un utilisateur."""
        query = "SELECT * FROM ingredients_favoris WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_favori(self, id_ingredient, id_utilisateur, **kwargs):
        """Met à jour un ingrédient favori."""
        query = (
            "UPDATE ingredients_favoris SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_ingredient = %s AND id_utilisateur = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_ingredient, id_utilisateur))

    def delete_favori(self, id_ingredient, id_utilisateur):
        """Supprime un ingrédient des favoris d'un utilisateur."""
        query = "DELETE FROM ingredients_favoris WHERE id_ingredient = %s AND id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))
