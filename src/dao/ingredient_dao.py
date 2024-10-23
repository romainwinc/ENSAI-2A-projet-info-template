from dao.db_connection import DBConnection
from models.ingredient import Ingredient
from utils.singleton import Singleton
from psycopg2 import sql
from dotenv import load_dotenv
import os


class IngredientDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def get_all_ingredients(self):
        """Récupère tous les ingrédients de la table 'ingredient'."""
        query = (
            """
            SELECT id_ingredient, nom_ingredient, description_ingredient
            FROM {}.ingredient
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()

        ingredients = []
        for row in rows:
            ingredient = {
                "id_ingredient": row["id_ingredient"],
                "nom_ingredient": row["nom_ingredient"],
                "description_ingredient": row["description_ingredient"],
            }
            ingredients.append(ingredient)

        return ingredients

    def get_ingredient_by_id(self, ingredient_id):
        """Récupère un ingrédient spécifique par son ID."""
        query = (
            """
            SELECT id_ingredient, nom_ingredient, description_ingredient
            FROM {}.ingredient
            WHERE id_ingredient = %s
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (ingredient_id,))
                row = cursor.fetchone()

        if row:
            ingredient = {
                "id_ingredient": row["id_ingredient"],
                "nom_ingredient": row["nom_ingredient"],
                "description_ingredient": row["description_ingredient"],
            }
            return ingredient
        return None

    def get_ingredient_by_nom(self, nom_ingredient):
        """Récupère un ingrédient spécifique par son nom."""
        query = (
            """
            SELECT id_ingredient, nom_ingredient, description_ingredient
            FROM {}.ingredient
            WHERE nom_ingredient = %s
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_ingredient,))
                row = cursor.fetchone()

        if row:
            ingredient = {
                "id_ingredient": row["id_ingredient"],
                "nom_ingredient": row["nom_ingredient"],
                "description_ingredient": row["description_ingredient"],
            }
            return ingredient
        return None

    def add_ingredient(self, ingredient: Ingredient) -> bool:
        """Ajout d'un nouvel ingrédient"""
        res = None
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO {}.ingredient "
                    "(nom_ingredient, description_ingredient) "
                    "VALUES (%(nom_ingredient)s, %(description_ingredient)s) "
                    "RETURNING id_ingredient;".format(self.schema),
                    {
                        "nom_ingredient": ingredient.nom_ingredient,
                        "description_ingredient": ingredient.description_ingredient,
                    },
                )
                res = cursor.fetchone()

        created = False
        if res:
            ingredient.id_ingredient = res["id_ingredient"]
            created = True

        return created

    def update_by_ingredient_id(self, ingredient_id, **kwargs):
        """Met à jour un ingrédient existant par son ID."""
        set_clause = sql.SQL(", ").join(
            sql.SQL("{} = %s").format(sql.Identifier(key)) for key in kwargs
        )

        query = sql.SQL(
            """
            UPDATE {}.ingredient
            SET {}
            WHERE id_ingredient = %s
            """
        ).format(sql.Identifier(self.schema), set_clause)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), ingredient_id))
                connection.commit()

    def update_by_ingredient_nom(self, nom_ingredient, **kwargs):
        """Met à jour un ingrédient existant par son nom."""
        # Construire dynamiquement la partie SET avec des Identifiers sécurisés
        set_clause = sql.SQL(", ").join(
            sql.SQL("{} = %s").format(sql.Identifier(key)) for key in kwargs
        )

        query = sql.SQL(
            """
            UPDATE {}.ingredient
            SET {}
            WHERE nom_ingredient = %s
            """
        ).format(sql.Identifier(self.schema), set_clause)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), nom_ingredient))
                connection.commit()

    def delete_ingredient(self, ingredient_id):
        """Supprime un ingrédient par son ID."""
        query = (
            """DELETE FROM {}.ingredient
                WHERE id_ingredient = %s
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (ingredient_id,))
                connection.commit()


if __name__ == "__main__":
    pass
    # print(IngredientDAO().get_all_ingredients()) # Marche

# print(IngredientDAO().get_ingredient_by_id(122)) # marche

# print(IngredientDAO().get_ingredient_by_nom("Eggs")) # Marche

# print("update par id")
# print(
#     IngredientDAO().update_by_ingredient_id(5, nom_ingredient="Tests Changement de Nom")
# )  # marche

# print("update par nom")
# print(
#     IngredientDAO().update_by_ingredient_nom("Eggs", description_ingredient="exemple d'oeufs")
# )  # marche

# print("Suppression")
# print(IngredientDAO().delete_ingredient(5))  # marche

# dao = IngredientDAO()
# try:
#     ingredient = Ingredient(
#         id_ingredient=None,
#         nom_ingredient="Ananas",
#         description_ingredient="Fruit",
#     )
#     dao.add_ingredient(ingredient)
# except ValueError as e:
#     print(e)
