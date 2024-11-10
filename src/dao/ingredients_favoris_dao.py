from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class IngredientsFavorisDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_ingredient_favori(self, nom_ingredient, id_utilisateur):
        """Ajoute un ingrédient aux favoris d'un utilisateur en utilisant le nom de l'ingrédient."""
        query = (
            """
            INSERT INTO {}.ingredients_favoris (id_ingredient, id_utilisateur)
            VALUES (
                (SELECT id_ingredient FROM {}.ingredient WHERE nom_ingredient = %s),
                %s
            )
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_ingredient, id_utilisateur))

    def get_favoris_by_user_id(self, id_utilisateur):
        """Récupère les noms des ingrédients favoris d'un utilisateur."""
        query = (
            """
            SELECT i.nom_ingredient
            FROM {}.ingredients_favoris f
            JOIN {}.ingredient i ON f.id_ingredient = i.id_ingredient
            WHERE f.id_utilisateur = %s
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return [row["nom_ingredient"] for row in cursor.fetchall()]

    def delete_ingredient_favori(self, nom_ingredient, id_utilisateur):
        """
        Supprime un ingrédient des favoris d'un utilisateur en utilisant le nom de l'ingrédient.
        """
        query = (
            """
            DELETE FROM {}.ingredients_favoris
            WHERE id_ingredient = (
                SELECT id_ingredient
                FROM {}.ingredient
                WHERE nom_ingredient = %s
            ) AND id_utilisateur = %s
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_ingredient, id_utilisateur))


if __name__ == "__main__":
    dao = IngredientsFavorisDAO()

    # # Exemple d'utilisation :
    # dao.add_ingredient_favori('Chicken', 1)
    # # Ajoute 'Chicken' aux favoris de l'utilisateur 1
    # print(dao.get_favoris_by_user_id(1))
    # # Renvoie les noms des ingrédients favoris de l'utilisateur 1
    # dao.delete_ingredient_favori('Chicken', 1)
    # # Supprime l'ingrédient 'Chicken' des favoris de l'utilisateur 1
