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
        query = (
            """
            INSERT INTO {}.consultation (id_recette, id_utilisateur, date_consultation)
            VALUES (%s, %s, %s)
        """
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        id_recette,
                        id_utilisateur,
                        date_consultation,
                    ),
                )

    def get_consultation(self, id_recette, id_utilisateur):
        """Récupère une consultation par ID recette et ID utilisateur."""
        query = (
            "SELECT * FROM {}.consultation WHERE id_recette = %s AND id_utilisateur = %s"
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))
                return cursor.fetchone()

    def update_consultation(self, id_recette, id_utilisateur, **kwargs):
        """Met à jour une consultation."""
        if not kwargs:
            return  # Si aucun champ à mettre à jour, ne fait rien.
        query = (
            (
                "UPDATE {}.consultation SET "
                + ", ".join([f"{key} = %s" for key in kwargs])
                + " WHERE id_recette = %s AND id_utilisateur = %s"
            )
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), id_recette, id_utilisateur))

    def delete_consultation(self, id_recette, id_utilisateur):
        """Supprime une consultation par ID recette et ID utilisateur."""
        query = (
            "DELETE FROM {}.consultation WHERE id_recette = %s AND id_utilisateur = %s"
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette, id_utilisateur))

    def get_consultations_by_utilisateur(self, id_utilisateur):
        """Récupère toutes les consultations d'un utilisateur donné."""
        query = ("SELECT * FROM {}.consultation WHERE id_utilisateur = %s").format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()


if __name__ == "__main__":
    pass
    # Tests des méthodes de ConsultationDAO (les décommenter pour tester)
    # ConsultationDAO().add_consultation(
    #     id_recette=1, id_utilisateur=1, date_consultation="2024-01-01"
    # )
    # print(ConsultationDAO().get_consultation(1, 1))
    # ConsultationDAO().update_consultation(1, 1, date_consultation="2024-01-02")
    # print(ConsultationDAO().get_consultation(1, 1))
    # ConsultationDAO().delete_consultation(1, 1)
    # print(ConsultationDAO().get_consultations_by_utilisateur(1))
