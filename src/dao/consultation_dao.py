from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class ConsultationDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_consultation(self, id_recette, id_utilisateur, date_consultation):
        """Ajoute une nouvelle consultation."""
        query = """
            INSERT INTO consultation (id_recette, id_utilisateur, date_consultation)
            VALUES (%s, %s, %s)
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur, date_consultation))

    def get_consultations_by_user_id(self, id_utilisateur):
        """Récupère les consultations pour un utilisateur donné."""
        query = "SELECT * FROM consultation WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_consultation(self, id_recette, id_utilisateur, **kwargs):
        """Met à jour une consultation."""
        query = (
            "UPDATE consultation SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_recette = %s AND id_utilisateur = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_recette, id_utilisateur))

    def delete_consultation(self, id_recette, id_utilisateur):
        """Supprime une consultation par recette et utilisateur."""
        query = "DELETE FROM consultation WHERE id_recette = %s AND id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))
