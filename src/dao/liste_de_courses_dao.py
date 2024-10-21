from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class ListeDeCoursesDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_liste_de_courses(self, id_ingredient, id_recette, id_utilisateur):
        """Ajoute un ingrédient à la liste de courses d'un utilisateur."""
        query = """
            INSERT INTO liste_de_courses (id_ingredient, id_recette, id_utilisateur)
            VALUES (%s, %s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_recette, id_utilisateur))

    def get_liste_by_user_id(self, id_utilisateur):
        """Récupère la liste de courses d'un utilisateur."""
        query = "SELECT * FROM liste_de_courses WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_liste(self, id_ingredient, id_recette, id_utilisateur, **kwargs):
        """Met à jour un ingrédient dans la liste de courses."""
        query = (
            "UPDATE liste_de_courses SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_ingredient = %s AND id_recette = %s AND id_utilisateur = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_ingredient, id_recette, id_utilisateur))

    def delete_from_liste(self, id_ingredient, id_recette, id_utilisateur):
        """Supprime un ingrédient de la liste de courses d'un utilisateur."""
        query = "DELETE FROM liste_de_courses WHERE id_ingredient = %s AND id_recette = %s AND id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_ingredient, id_recette, id_utilisateur))
