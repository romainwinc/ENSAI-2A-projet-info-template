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
        query = (
            """
            INSERT INTO {}.demande (
                id_utilisateur,
                type_demande,
                attribut_modifie,
                attribut_corrige,
                commentaire_demande
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_demande
            """
        ).format(self.schema)
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
                return cursor.fetchone()["id_demande"]

    def get_demandes_with_role(self):
        """
        Récupère toutes les demandes où attribut_modifie est égal à 'role'.

        Returns:
            List[dict]: Liste des demandes correspondantes.
        """
        query = (
            """
            SELECT id_demande, id_utilisateur, type_demande, attribut_modifie, 
                attribut_corrige, commentaire_demande
            FROM {}.demande
            WHERE attribut_modifie = %s
            """
        ).format(self.schema)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, ("role",))
                rows = cursor.fetchall()

        demandes = []
        for row in rows:
            demande = {
                "id_demande": row["id_demande"],
                "id_utilisateur": row["id_utilisateur"],
                "type_demande": row["type_demande"],
                "attribut_modifie": row["attribut_modifie"],
                "attribut_corrige": row["attribut_corrige"],
                "commentaire_demande": row["commentaire_demande"],
            }
            demandes.append(demande)

        return demandes

    def get_demande_by_id(self, demande_id):
        """Récupère une demande par son ID."""
        query = ("SELECT * FROM {}.demande WHERE id_demande = %s").format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (demande_id,))
                return cursor.fetchone()

    def get_demande_by_id_utilisateur(self, id_utilisateur):
        """Récupère toutes les demandes d'un utilisateur donné."""
        query = ("SELECT * FROM {}.demande WHERE id_utilisateur = %s").format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (id_utilisateur,))
                return cursor.fetchall()

    def update_demande(self, demande_id, **kwargs):
        """Met à jour une demande."""
        query = (
            (
                "UPDATE {}.demande SET "
                + ", ".join([f"{key} = %s" for key in kwargs])
                + " WHERE id_demande = %s"
            )
        ).format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (*kwargs.values(), demande_id))

    def delete_demande(self, demande_id):
        """Supprime une demande par son ID."""
        query = ("DELETE FROM {}.demande WHERE id_demande = %s").format(self.schema)
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (demande_id,))


if __name__ == "__main__":
    pass
    # print(
    #     DemandeDAO().add_demande(
    #         id_utilisateur=1,
    #         type_demande="modification utilisateur",
    #         attribut_modifie="nom",
    #         attribut_corrige="Xavier",
    #         commentaire_demande="changer nom de l'utilisateur 1 par Xavier",
    #     )
    # )  # Marche

    # print(
    #     DemandeDAO().update_demande(
    #         demande_id=2, type_demande="Modification", attribut_corrige="Pierre"
    #     )
    # ) # Marche

    # print(DemandeDAO().get_demande_by_id(2)) # Marche

    # print(DemandeDAO().delete_demande(2)) # Marche

    # print(DemandeDAO().get_demande_by_id_utilisateur(1))
