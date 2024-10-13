from dao.db_connection import DBConnection
from utils.singleton import Singleton


class IngredientDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def get_all_ingredients(self):
        """Récupère tous les ingrédients de la table 'ingredient'."""
        query = """
            SELECT id_ingredient, nom_ingredient, description_ingredient
            FROM ingredient
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

        ingredients = []
        for row in rows:
            ingredient = {
                "id_ingredient": row[0],
                "nom_ingredient": row[1],
                "description_ingredient": row[2],
            }
            ingredients.append(ingredient)

        return ingredients

    def get_ingredient_by_id(self, ingredient_id):
        """Récupère un ingrédient spécifique par son ID."""
        query = """
            SELECT id_ingredient, nom_ingredient, description_ingredient
            FROM ingredient
            WHERE id_ingredient = %s
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (ingredient_id,))
                row = cursor.fetchone()

        if row:
            ingredient = {
                "id_ingredient": row[0],
                "nom_ingredient": row[1],
                "description_ingredient": row[2],
            }
            return ingredient
        return None

    def add_ingredient(self, nom_ingredient, description_ingredient):
        """Ajoute un nouvel ingrédient dans la table 'ingredient'."""
        query = """
            INSERT INTO ingredient (nom_ingredient, description_ingredient)
            VALUES (%s, %s)
            RETURNING id_ingredient
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_ingredient, description_ingredient))
                ingredient_id = cursor.fetchone()[0]
        return ingredient_id

    def update_ingredient(self, ingredient_id, **kwargs):
        """Met à jour un ingrédient existant."""
        query = "UPDATE ingredient SET "
        query += ", ".join([f"{key} = %s" for key in kwargs])
        query += " WHERE id_ingredient = %s"

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), ingredient_id))

    def delete_ingredient(self, ingredient_id):
        """Supprime un ingrédient par son ID."""
        query = "DELETE FROM ingredient WHERE id_ingredient = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (ingredient_id,))
