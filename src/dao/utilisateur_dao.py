import logging
from typing import Optional
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from models.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    def __init__(self):
        self.connection = DBConnection().connection

    def add_user(self, utilisateur: Utilisateur) -> bool:
        """Ajout d'un utilisateur

        Parameters
        ----------
        utilisateur : Utilisateur
            un nouvel utilisateur

        Returns
        -------
        created : bool
            renvoie si l'utilisateur est créé
        """
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
        """Trouver un utilisateur avec un nom et mot de passe

        Parameters
        ----------
        nom : str
            correspond au nom d'utilisateur
        mdp : str
            correspond au mot de passe de l'utilisateur

        Returns
        -------
        res : Optional[int]

        """
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
        print(upgrade)
        query = (
            "UPDATE projet_informatique.utilisateur SET role= %(role)s"
            + " WHERE id_utilisateur = %(id_utilisateur)s "
        )
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, {"id_utilisateur": id_utilisateur, "role": upgrade})

    def delete_user(self, id_utilisateur):
        """Supprime le compte d'un utilisateur"""

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM projet_informatique.utilisateur "
                    "WHERE id_utilisateur = %(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )

    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """se connecter grâce à son pseudo et son mot de passe

        Parameters
        ----------
        pseudo : str
            pseudo de l'utilisateur que l'on souhaite trouver
        mdp : str
            mot de passe de l'utilisateur

        Returns
        -------
        joueur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        res = None
        utilisateur = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM projet_informatique.utilisateur                      "
                        " WHERE (nom_utilisateur = %(nom_utilisateur)s         "
                        "   AND mot_de_passe = %(mot_de_passe)s);              ",
                        {"nom_utilisateur": pseudo, "mot_de_passe": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        if res:
            utilisateur = Utilisateur(
                nom_utilisateur=res["nom_utilisateur"],
                mot_de_passe=res["mot_de_passe"],
                id_utilisateur=res["id_utilisateur"],
                role=res["role"],
                date_inscription=res["date_inscription"],
            )

        return utilisateur

    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les utilisateurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateurs : list[Utilisateur]
        renvoie la liste de tous les utilisateurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM projet_informatique.utilisateur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    nom_utilisateur=row["nom_utilisateur"],
                    mot_de_passe=row["mot_de_passe"],
                    id_utilisateur=row["id_utilisateur"],
                    role=row["role"],
                    date_inscription=row["date_inscription"],
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs
