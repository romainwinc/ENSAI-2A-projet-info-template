from models.recette import Recette
from datetime import datetime
from models.ingredient import Ingredient


class Utilisateur:
    """
    Représente un utilisateur connecté avec des informations personnelles,
    des préférences alimentaires et une liste de courses.

    Parameters
    ----------
    nom : str
        Le nom de l'utilisateur.
    prenom : str
        Le prénom de l'utilisateur.
    username : str
        Le nom d'utilisateur pour la connexion.
    password : str
        Le mot de passe de l'utilisateur.
    role
    """

    def __init__(
        self,
        nom_utilisateur: str,
        mot_de_passe: str,
        id_utilisateur: str = None,
        role: str = "Non connecté",
        date_inscription: datetime = None,
    ) -> None:
        self.nom_utilisateur = nom_utilisateur
        self.mot_de_passe = mot_de_passe
        self.id_utilisateur = id_utilisateur
        self.role = role
        self.date_inscription = date_inscription

    def __repr__(self) -> str:
        """
        Renvoie une représentation lisible de l'utilisateur connecté.
        """
        return (
            f"Connecte(identifiant={self.id_utilisateur}, nom d'utilisateur={self.nom_utilisateur},"
            f"mot de passe ={self.mot_de_passe},ingredient_favori={self.ingredient_favori},"
            f"recette_favorite={self.recette_favorite},liste_course={self.liste_course}, "
            f"liste_ingredient_favori={self.liste_ingredient_favori}, "
            f"liste_ingredient_non_desires={self.liste_ingredient_non_desires}, role={self.grade})"
        )
