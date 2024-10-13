from dao.db_connection import DBConnection
from utils.singleton import Singleton


class IngredientsNonDesiresDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_ingredient_non_desire(self, id_ingredient, id_utilisateur):
        """Ajoute un ingrédient non désiré pour un utilisateur."""
        query = """
            INSERT INTO ingredients_non_desires (id_ingredient, id_utilisateur)
            VALUES (%s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))

    def get_non_desires_by_user_id(self, id_utilisateur):
        """Récupère les ingrédients non désirés d'un utilisateur."""
        query = "SELECT * FROM ingredients_non_desires WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_non_desire(self, id_ingredient, id_utilisateur, **kwargs):
        """Met à jour un ingrédient non désiré."""
        query = (
            "UPDATE ingredients_non_desires SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_ingredient = %s AND id_utilisateur = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_ingredient, id_utilisateur))

    def delete_non_desire(self, id_ingredient, id_utilisateur):
        """Supprime un ingrédient non désiré d'un utilisateur."""
        query = (
            "DELETE FROM ingredients_non_desires WHERE id_ingredient = %s AND id_utilisateur = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))
