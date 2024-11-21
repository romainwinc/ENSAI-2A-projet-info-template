from datetime import datetime


class Utilisateur:
    """
    Représente un utilisateur avec ses informations personnelles, son rôle,
    et sa date d'inscription.

    Attributs :
        nom_utilisateur (str): Le nom de l'utilisateur.
        mot_de_passe (str): Le mot de passe de l'utilisateur.
        id_utilisateur (str ou None): L'identifiant unique de l'utilisateur (optionnel).
        role (str): Le rôle de l'utilisateur (par défaut "Non connecté").
        date_inscription (datetime ou None): La date d'inscription de l'utilisateur (optionnel).
    """

    def __init__(
        self,
        nom_utilisateur: str,
        mot_de_passe: str,
        id_utilisateur: str = None,
        role: str = "Non connecté",
        date_inscription: datetime = None,
    ) -> None:
        """
        Initialise un utilisateur avec ses informations personnelles.

        Paramètres :
            nom_utilisateur (str): Le nom de l'utilisateur.
            mot_de_passe (str): Le mot de passe de l'utilisateur.
            id_utilisateur (str, optionnel): L'identifiant unique de l'utilisateur. Par défaut, c'est None.
            role (str, optionnel): Le rôle de l'utilisateur. Par défaut, c'est "Non connecté".
            date_inscription (datetime, optionnel): La date d'inscription de l'utilisateur. Par défaut, c'est None.
        """
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.id_utilisateur = id_utilisateur
        self.role = role
        self.date_inscription = date_inscription

    def __repr__(self) -> str:
        """
        Renvoie une représentation lisible de l'utilisateur connecté.

        Retourne :
            str: Une chaîne représentant l'utilisateur, incluant son identifiant, son nom d'utilisateur,
                 son mot de passe et son rôle.
        """
        return (
            f"Utilisateur(identifiant={self.id_utilisateur}, nom_utilisateur={self.nom_utilisateur}, "
            f"mot_de_passe={self.mot_de_passe}, role={self.role})"
        )
