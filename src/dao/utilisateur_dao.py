from typing import Optional
from Utils.singleton import Singleton
from dao.db_connection import DBConnection
from models.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):

    def add_user(self, utilisateur: Utilisateur) -> bool:
        """Ajout d'un utilisateur"""
        created = False

        # Get the id user
        id_utilisateur = UtilisateurDao().find_id_user(utilisateur.nom_utilisateur)
        if id_utilisateur is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO utilisateur (id_utilisateur, nom_utilsateur,       "
                    " mot_de_passe, role, date_inscription)                         "
                    "VALUES                                                         "
                    "(%(id_utilisateur)s, %(nom_utilsateur)s, %(mot_de_passe)s,     "
                    " %(role)s, %(date_inscription)s)                               "
                    "RETURNING id_utilisateur;",
                    {
                        "id_utilisateur": id_utilisateur,
                        "nom_utilsateur": utilisateur.nom_utilisateur,
                        "mot_de_passe": utilisateur.mot_de_passe,
                        "role": utilisateur.role,
                        "date_inscription": utilisateur.date_inscription,
                    },
                )
                res = cursor.fetchone()
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    def find_id_user(self, nom: str) -> Optional[int]:
        """Trouver un utilisateur avec un nom"""
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_utilisateur                     "
                    "FROM projet_informatique.utilisateur                     "
                    "WHERE nom_utilisateur = %(nom_utilisateur)s ",
                    {"nom_utilisateur": nom},
                )
                res = cursor.fetchone()

        if res:
            return res["id_utilisateur"]

    def update_user(self, id_utilisateur, upgrade):
        """Met à jour une association recette-ingredient."""
        query = "UPDATE utilisateur SET role= %(upgrade)s" + " WHERE id_utilisateur = %s "
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    query,
                )

    def delete_user(self, id_utilisateur):
        """Supprime le compte d'un utilisateur"""

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM utilisateur WHERE id_utilisateur = %s", id_utilisateur)
