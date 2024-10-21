from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dotenv import load_dotenv
import os


class DemandeDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection
        load_dotenv()
        self.schema = os.getenv("POSTGRES_SCHEMA")

    def add_demande(
        self, id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande
    ):
        """Ajoute une nouvelle demande."""
        query = """
            INSERT INTO demande (id_utilisateur, type_demande, attribut_modifie, attribut_corrige, commentaire_demande)
            VALUES (%s, %s, %s, %s, %s) RETURNING id_demande
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        id_utilisateur,
                        type_demande,
                        attribut_modifie,
                        attribut_corrige,
                        commentaire_demande,
                    ),
                )
                return cursor.fetchone()[0]

    def get_demande_by_id(self, demande_id):
        """Récupère une demande par son ID."""
        query = "SELECT * FROM demande WHERE id_demande = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (demande_id,))
                return cursor.fetchone()

    def update_demande(self, demande_id, **kwargs):
        """Met à jour une demande."""
        query = (
            "UPDATE demande SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_demande = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), demande_id))

    def delete_demande(self, demande_id):
        """Supprime une demande par son ID."""
        query = "DELETE FROM demande WHERE id_demande = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (demande_id,))
