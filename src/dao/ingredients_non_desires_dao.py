from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class IngredientsNonDesiresDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_ingredient_non_desire(self, id_ingredient, id_utilisateur):
        """Ajoute un ingrédient à la liste des non désirés d'un utilisateur."""
        query = (
            """
            INSERT INTO {}.ingredients_non_desires (id_ingredient, id_utilisateur)
            VALUES (%s, %s)
            """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))

    def get_non_desires_by_user_id(self, id_utilisateur):
        """Récupère les noms des ingrédients non désirés d'un utilisateur."""
        query = (
            """
            SELECT i.nom_ingredient 
            FROM {}.ingredients_non_desires nd
            JOIN {}.ingredient i ON nd.id_ingredient = i.id_ingredient
            WHERE nd.id_utilisateur = %s
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return [row["nom_ingredient"] for row in cursor.fetchall()]

    def delete_ingredient_non_desire(self, id_ingredient, id_utilisateur):
        """Supprime un ingrédient de la liste des non désirés d'un utilisateur."""
        query = (
            "DELETE FROM {}.ingredients_non_desires WHERE id_ingredient = %s AND id_utilisateur = %s"
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_utilisateur))


if __name__ == "__main__":
    dao = IngredientsNonDesiresDAO()

    # # Exemple d'utilisation :
    # dao.add_ingredient_non_desire(
    #     4, 1
    # )  # Ajoute l'ingrédient 4 à la liste des non désirés de l'utilisateur 1
    # print(
    #     dao.get_non_desires_by_user_id(1)
    # )  # Renvoie les noms des ingrédients non désirés de l'utilisateur 1
