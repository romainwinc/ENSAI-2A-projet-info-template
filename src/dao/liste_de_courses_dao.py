from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class ListeDeCoursesDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_ingredient_to_liste(self, nom_ingredient, id_utilisateur):
        """Ajoute un ingrédient à la liste de courses d'un utilisateur en utilisant le nom de l'ingrédient."""
        query = (
            """
            INSERT INTO {}.liste_de_courses (id_ingredient, id_utilisateur)
            VALUES (
                (SELECT id_ingredient FROM {}.ingredient WHERE nom_ingredient = %s), 
                %s
            )
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (nom_ingredient, id_utilisateur))

    def get_liste_de_courses_by_user_id(self, id_utilisateur):
        """Récupère les ingrédients de la liste de courses d'un utilisateur."""
        query = (
            """
            SELECT i.nom_ingredient
            FROM {}.liste_de_courses lc
            JOIN {}.ingredient i ON lc.id_ingredient = i.id_ingredient
            WHERE lc.id_utilisateur = %s
            """
        ).format(self.schema, self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return [row["nom_ingredient"] for row in cursor.fetchall()]

    def delete_ingredient_from_liste(self, nom_ingredient, id_utilisateur):
        """Supprime un ingrédient de la liste de courses d'un utilisateur en utilisant le nom de l'ingrédient."""
        query = (
            """
            DELETE FROM {}.liste_de_courses 
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
    dao = ListeDeCoursesDAO()

    # Exemple d'utilisation :
    dao.add_ingredient_to_liste(
        "Chicken", 1
    )  # Ajoute 'Tomate' à la liste de courses de l'utilisateur 1
    print(dao.get_liste_de_courses_by_user_id(1))  # Renvoie la liste de courses de l'utilisateur 1
    dao.delete_ingredient_from_liste(
        "Chicken", 1
    )  # Supprime l'ingrédient 'Tomate' de la liste de courses de l'utilisateur 1
