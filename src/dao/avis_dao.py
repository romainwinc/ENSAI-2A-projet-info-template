from dao.db_connection import DBConnection
from utils.singleton import Singleton


class AvisDAO(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_avis(
        self,
        id_recette,
        id_utilisateur,
        titre_avis,
        nom_auteur,
        date_publication,
        commentaire,
        note,
    ):
        """Ajoute un nouvel avis."""
        query = """
            INSERT INTO avis (id_recette, id_utilisateur, titre_avis, nom_auteur, date_publication, commentaire, note)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id_avis
        """
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                    (
                        id_recette,
                        id_utilisateur,
                        titre_avis,
                        nom_auteur,
                        date_publication,
                        commentaire,
                        note,
                    ),
                )
                return cursor.fetchone()[0]

    def get_avis_by_recette_id(self, id_recette):
        """Récupère les avis pour une recette donnée."""
        query = "SELECT * FROM avis WHERE id_recette = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_recette,))
                return cursor.fetchall()

    def get_avis_by_user_id(self, id_utilisateur):
        """Récupère les avis d'un utilisateur donné."""
        query = "SELECT * FROM avis WHERE id_utilisateur = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_avis(self, avis_id, **kwargs):
        """Met à jour un avis."""
        query = (
            "UPDATE avis SET "
            + ", ".join([f"{key} = %s" for key in kwargs])
            + " WHERE id_avis = %s"
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), avis_id))

    def delete_avis(self, avis_id):
        """Supprime un avis par son ID."""
        query = "DELETE FROM avis WHERE id_avis = %s"
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (avis_id,))
