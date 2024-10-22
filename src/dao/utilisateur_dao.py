from typing import Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from models.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_user(self, utilisateur: Utilisateur) -> bool:
        """Ajout d'un utilisateur"""
        res = None
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projet_informatique.utilisateur "
                    "(nom_utilisateur, mot_de_passe, role, date_inscription) "
                    "VALUES                                                         "
                    "(%(nom_utilisateur)s, %(mot_de_passe)s,     "
                    " %(role)s, %(date_inscription)s)                               "
                    "RETURNING id_utilisateur;",
                    {
                        "nom_utilisateur": utilisateur.nom_utilisateur,
                        "mot_de_passe": utilisateur.mot_de_passe,
                        "role": utilisateur.role,
                        "date_inscription": utilisateur.date_inscription,
                    },
                )
                res = cursor.fetchone()
        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    def find_id_user(self, nom: str, mdp: str) -> Optional[int]:
        """Trouver un utilisateur avec un nom et mot de passe"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_utilisateur                     "
                    "FROM projet_informatique.utilisateur                     "
                    "WHERE (nom_utilisateur = %(nom)s "
                    "AND mot_de_passe = %(mdp)s)  ",
                    {"nom": nom, "mdp": mdp},
                )
                res = cursor.fetchone()

        if res:
            return res["id_utilisateur"]

    def update_user(self, id_utilisateur: str, upgrade: str):
        """Met à jour une association recette-ingredient."""
        query = (
            "UPDATE projet_informatique.utilisateur SET role= %(upgrade)s"
            + " WHERE id_utilisateur = %s "
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                )

    def delete_user(self, id_utilisateur):
        """Supprime le compte d'un utilisateur"""

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projet_informatique.utilisateur WHERE id_utilisateur = %s",
                    id_utilisateur,
                )
