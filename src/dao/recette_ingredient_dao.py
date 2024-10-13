from dao.db_connection import DBConnection
from utils.singleton import Singleton


class RecetteIngredientDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_recette_ingredient(self, id_recette, id_ingredient, mesure):
        """Ajoute une association recette-ingredient."""
        query = """
            INSERT INTO recette_ingredient (id_recette, id_ingredient, mesure)
            VALUES (%s, %s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_ingredient, mesure))

    def get_ingredients_by_recette_id(self, id_recette):
        """Récupère les ingrédients d'une recette."""
        query = "SELECT * FROM recette_ingredient WHERE id_recette = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette,))
                return cursor.fetchall()

    def update_recette_ingredient(self, id_recette, id_ingredient, **kwargs):
        """Met à jour une association recette-ingredient."""
        query = (
            "UPDATE recette_ingredient SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_recette = %s AND id_ingredient = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_recette, id_ingredient))

    def delete_recette_ingredient(self, id_recette, id_ingredient):
        """Supprime une association recette-ingredient."""
        query = "DELETE FROM recette_ingredient WHERE id_recette = %s AND id_ingredient = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_ingredient))
